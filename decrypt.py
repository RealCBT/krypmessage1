# import required module
from cryptography.fernet import Fernet
# key generation
class Decrypt():
    def __init__(self, filepath):
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            
        fernet = Fernet(key)
 
        # opening the encrypted file
        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        with open(filepath, 'wb') as dec_file:
            dec_file.write(decrypted)