from Crypto.PublicKey import RSA

new_key = RSA.generate(4096, e = 65537)

private_key = new_key.exportKey("PEM")

public_key = new_key.publickey().exportKey("PEM")

print("Private Key: ", private_key)

fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print("Public Key: ", public_key)

fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

