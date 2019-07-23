from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib

def decrypt_blob(encrypted_blob, private_key):

    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    encrypted_blob = base64.b64decode(encrypted_blob)

    zobj = zlib.decompressobj()
    chunk_size = 512
    offset = 0
    decrypted = b""

    while offset < len(encrypted_blob):

        chunk = encrypted_blob[offset : offset + chunk_size]

        decrypted += rsakey.decrypt(chunk)

        offset += chunk_size

    return zobj.decompress(decrypted)

fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

fd = open("encrypted_image.jpg", "rb")
encrypted_blob = fd.read()
fd.close()

decrypted_image = decrypt_blob(encrypted_blob, private_key)


fd = open("decrypted_img.jpg", "wb")
fd.write(decrypted_image)
fd.close()