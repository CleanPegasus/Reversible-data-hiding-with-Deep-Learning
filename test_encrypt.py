from Crypto.Cipher import AES
from Crypto import Random

def encrypt(input_data, key, iv):

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    return enc_data


fd = open("key.pem", "rb")
key = fd.read()
fd.close()

fd = open("iv.pem", "rb")
iv = fd.read()
fd.close()


input_file = open("image.jpg", "rb")
input_data = input_file.read()
input_file.close()

enc_data = encrypt(input_data, key, iv)

enc_file = open("encrypted.enc", "wb")
enc_file.write(enc_data)
enc_file.close()