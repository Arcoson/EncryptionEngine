import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from exceptions import EncryptionError, DecryptionError

class CryptoHandler:
    def __init__(self):
        self.SALT_SIZE = 16
        self.IV_SIZE = 16
        self.KEY_SIZE = 32
        self.ITERATIONS = 100000

    def derive_key(self, password: str, salt: bytes = None) -> tuple:
        if not salt:
            salt = os.urandom(self.SALT_SIZE)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=self.KEY_SIZE,
            salt=salt,
            iterations=self.ITERATIONS,
            backend=default_backend()
        )
        
        key = kdf.derive(password.encode())
        return key, salt

    def encrypt_data(self, data: bytes, password: str) -> bytes:
        try:
            key, salt = self.derive_key(password)
            iv = os.urandom(self.IV_SIZE)
            cipher = Cipher(
                algorithms.AES(key),
                modes.GCM(iv),
                backend=default_backend()
            )
            encryptor = cipher.encryptor()
            
            ciphertext = encryptor.update(data) + encryptor.finalize()
            
            return b64encode(salt + iv + encryptor.tag + ciphertext)
        
        except Exception as e:
            raise EncryptionError(f"Encryption failed: {str(e)}")

    def decrypt_data(self, encrypted_data: bytes, password: str) -> bytes:
        try:
            raw_data = b64decode(encrypted_data)
            
            salt = raw_data[:self.SALT_SIZE]
            iv = raw_data[self.SALT_SIZE:self.SALT_SIZE + self.IV_SIZE]
            tag = raw_data[self.SALT_SIZE + self.IV_SIZE:self.SALT_SIZE + self.IV_SIZE + 16]
            ciphertext = raw_data[self.SALT_SIZE + self.IV_SIZE + 16:]
            
            key, _ = self.derive_key(password, salt)
            
            cipher = Cipher(
                algorithms.AES(key),
                modes.GCM(iv, tag),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            
            return decryptor.update(ciphertext) + decryptor.finalize()
        
        except Exception as e:
            raise DecryptionError(f"Decryption failed: {str(e)}")
