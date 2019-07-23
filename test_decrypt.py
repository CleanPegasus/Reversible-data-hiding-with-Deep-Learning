from Crypto.Cipher import AES
from Crypto import Random

def decrypt(enc_data, key, iv):

    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_data = cfb_decipher.decrypt(enc_data)

    return decrypted_data


fd = open("key.pem", "rb")
key = fd.read()
fd.close()

fd = open("iv.pem", "rb")
iv = fd.read()
fd.close()

enc_file2 = open("encrypted.enc", "rb")
enc_data2 = enc_file2.read()
enc_file2.close()


plain_data = decrypt(enc_data2, key, iv)
#print(plain_data)

output_file = open("output.jpg", "wb")
output_file.write(plain_data)
output_file.close()