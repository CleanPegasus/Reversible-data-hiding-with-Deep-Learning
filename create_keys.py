from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

fd = open("key.pem", "wb")
fd.write(key)
fd.close()

fd = open("iv.pem", "wb")
fd.write(iv)
fd.close()