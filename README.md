# EncryptionEngine

A secure command-line tool for file encryption and management using AES-256-GCM encryption.

## Features

- **Strong Encryption**: Uses AES-256-GCM for secure file encryption
- **Password-Based Security**: Files are encrypted using user-provided passwords
- **File Management**: Store, retrieve, list, and delete encrypted files
- **Secure Key Derivation**: Implements PBKDF2 with SHA-256 for key derivation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Arcoson/EncryptionEngine.git
cd encryption-engine
```

2. Install required dependencies:
```bash
pip install cryptography
```

## Usage

### Encrypting a File
```bash
python encryption_engine.py store <file_path> -p <password>
```

### Decrypting a File
```bash
python encryption_engine.py retrieve <encrypted_file_path> <output_path> -p <password>
```

### Listing Encrypted Files
```bash
python encryption_engine.py list
```

### Deleting an Encrypted File
```bash
python encryption_engine.py delete <encrypted_file_path>
```

## Security Considerations

- **Password Strength**: Use strong, unique passwords for each encrypted file
- **Password Storage**: Passwords are not stored; you must remember them to decrypt files
- **Key Derivation**: PBKDF2 with 100,000 iterations is used for secure key derivation
- **Encryption Algorithm**: AES-256-GCM provides both confidentiality and authenticity

## Command Reference

### `store`
Encrypts and stores a file
```bash
python encryption_engine.py store <file> -p <password>
```

### `retrieve`
Decrypts and retrieves a file
```bash
python encryption_engine.py retrieve <encrypted_file> <output_file> -p <password>
```

### `list`
Lists all encrypted files
```bash
python encryption_engine.py list
```

### `delete`
Deletes an encrypted file
```bash
python encryption_engine.py delete <encrypted_file>
```

## Technical Details

- **Encryption**: AES-256-GCM
- **Key Derivation**: PBKDF2-HMAC-SHA256 with 100,000 iterations
- **Salt Size**: 16 bytes
- **IV Size**: 16 bytes
- **Key Size**: 32 bytes


## License

This project is licensed under the MIT License - see the LICENSE file for details.
