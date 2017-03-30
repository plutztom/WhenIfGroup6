import base64
import hashlib

class Encrypt:
    def __init__(self,key):
        self.key = bytes(key,'utf-8')
        
        

    def encrypt(self,message,key_size=256):
        message = (str(message) + ("\0" * ((AES.block_size - len(message) % AES.block_size))))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(bytes(message,'utf-8'))

    def decrypt(self,ciphertext):
        if(len(ciphertext) == 0): return ''
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.decode("utf-8",'ignore').rstrip("\0")
