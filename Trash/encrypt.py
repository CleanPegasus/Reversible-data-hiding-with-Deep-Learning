from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
import cv2

def encrypt_blob(blob, public_key):

    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    zobj = zlib.compressobj()
    blob = zobj.compress

    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = b""

    while not end_loop:

        chunk = blob[offset : offset + chunk_size]

        if len(chunk) % chunk_size != 0:

            end_loop = True

            chunk += b"" * (chunk_size - len(chunk))

        encrypted += rsa_key.encrypt(chunk)

        offset += chunk_size

        return base64.b64encode(encrypted)

fd = open("public_key.pem", "rb")
publick_key = fd.read()
fd.close()

fd = open("image.jpg", "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, publick_key)

fd = open("encrypted_image.jpg", "wb")
fd.write(encrypted_blob)
fd.close()

