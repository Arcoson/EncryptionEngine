class EncryptionError(Exception):
    """Base exception for encryption-related errors"""
    pass

class DecryptionError(Exception):
    """Base exception for decryption-related errors"""
    pass

class FileOperationError(Exception):
    """Base exception for file operation errors"""
    pass

class AuthenticationError(Exception):
    """Base exception for authentication-related errors"""
    pass
