# import required module
from cryptography.fernet import Fernet
# key generation
class Encrypt():
    def __init__(self, filepath):
        key = Fernet.generate_key()

        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        # using the generated key
        fernet = Fernet(key)
        
        # opening the original file to encrypt
        with open(filepath, 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and
        # writing the encrypted data
        with open(filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            
"""key = Fernet.generate_key()

        # string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
        
        # using the generated key
fernet = Fernet(key)
        
        # opening the original file to encrypt
with open('C:\\Users\\tiwar\\Desktop\\data2.csv', 'rb') as file:
    original = file.read()
            
        # encrypting the file
encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and
        # writing the encrypted data
with open('C:\\Users\\tiwar\\Desktop\\data2.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)"""