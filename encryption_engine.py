import argparse
import sys
from pathlib import Path
from file_manager import FileManager
from exceptions import EncryptionError, DecryptionError, FileOperationError

def create_parser():
    parser = argparse.ArgumentParser(
        description="EncryptionEngine - Secure file encryption and management tool"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    store_parser = subparsers.add_parser("store", help="Encrypt and store a file")
    store_parser.add_argument("file", help="Path to the file to encrypt")
    store_parser.add_argument("--password", "-p", required=True, help="Encryption password")
    
    retrieve_parser = subparsers.add_parser("retrieve", help="Decrypt and retrieve a file")
    retrieve_parser.add_argument("file", help="Path to the encrypted file")
    retrieve_parser.add_argument("output", help="Output path for decrypted file")
    retrieve_parser.add_argument("--password", "-p", required=True, help="Decryption password")
    
    subparsers.add_parser("list", help="List all encrypted files")
    
    delete_parser = subparsers.add_parser("delete", help="Delete an encrypted file")
    delete_parser.add_argument("file", help="Path to the encrypted file to delete")
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    file_manager = FileManager()
    
    try:
        if args.command == "store":
            if not Path(args.file).exists():
                print(f"Error: File '{args.file}' does not exist")
                return
            
            stored_path = file_manager.store_file(args.file, args.password)
            print(f"File encrypted and stored successfully at: {stored_path}")

        elif args.command == "retrieve":
            if not Path(args.file).exists():
                print(f"Error: Encrypted file '{args.file}' does not exist")
                return
            
            output_path = file_manager.retrieve_file(args.file, args.password, args.output)
            print(f"File decrypted successfully to: {output_path}")

        elif args.command == "list":
            files = file_manager.list_files()
            if not files:
                print("No encrypted files found")
            else:
                print("Encrypted files:")
                for file in files:
                    print(f"- {file}")

        elif args.command == "delete":
            if not Path(args.file).exists():
                print(f"Error: File '{args.file}' does not exist")
                return
            
            file_manager.delete_file(args.file)
            print(f"File deleted successfully: {args.file}")

    except (EncryptionError, DecryptionError, FileOperationError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)

if __name__ == "__main__":
    main()
