from hashlib import sha256
from base64 import b64decode, b64encode
from os import urandom

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = sha256(key.encode('utf-8')).digest()

    def encrypt(self, data):
        iv = urandom(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


def keyEncryptor(data, pwd='', keyFile='key'):
    # Generate Key.
    print("\nGenerating Key... ", end='')
    encrpyted_data = AESCipher(pwd).encrypt(data).decode('utf-8')
    print("Done.")

    print("Writing Key File... ", end='')
    # Write the Key File.
    with open(keyFile, 'w') as key:
        key.write(encrpyted_data)
    print("Done.")


def keyDecryptor(keyFile='key', pwd=''):
    try:

        with open(keyFile, 'r') as key:
            print("\nReading key... ", end='')
            encrpyted_data = key.read()

        decrypted_data = AESCipher(pwd).decrypt(encrpyted_data).decode('utf-8')
        print("Done")

        return decrypted_data
    except Exception:
        print("\n Failed!")
