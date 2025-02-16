import os
from pathlib import Path
from typing import List
from crypto_utils import CryptoHandler
from exceptions import FileOperationError

class FileManager:
    def __init__(self, storage_dir: str = ".encrypted_files"):
        self.storage_dir = Path(storage_dir)
        self.crypto_handler = CryptoHandler()
        self._init_storage()

    def _init_storage(self):
        try:
            self.storage_dir.mkdir(exist_ok=True)
        except Exception as e:
            raise FileOperationError(f"Failed to create storage directory: {str(e)}")

    def store_file(self, file_path: str, password: str) -> str:
        try:
            with open(file_path, 'rb') as f:
                data = f.read()

            encrypted_data = self.crypto_handler.encrypt_data(data, password)

            original_name = Path(file_path).name
            encrypted_path = self.storage_dir / f"{original_name}.encrypted"

            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)

            return str(encrypted_path)

        except Exception as e:
            raise FileOperationError(f"Failed to store file: {str(e)}")

    def retrieve_file(self, file_path: str, password: str, output_path: str) -> str:
        try:
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()

            decrypted_data = self.crypto_handler.decrypt_data(encrypted_data, password)

            with open(output_path, 'wb') as f:
                f.write(decrypted_data)

            return output_path

        except Exception as e:
            raise FileOperationError(f"Failed to retrieve file: {str(e)}")

    def list_files(self) -> List[str]:
        try:
            return [str(f.name) for f in self.storage_dir.glob("*.encrypted")]
        except Exception as e:
            raise FileOperationError(f"Failed to list files: {str(e)}")

    def delete_file(self, file_path: str):
        try:
            Path(file_path).unlink()
        except Exception as e:
            raise FileOperationError(f"Failed to delete file: {str(e)}")
