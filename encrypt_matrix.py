import numpy as np
from numpy.linalg import inv
from sympy import Matrix

def generate_key():

    key1 = np.random.randint(0, 10, size = (9, 9))
    key2 = np.random.randint(0, 10, size = (9, 9))
    key3 = np.random.randint(0, 10, size = (9, 9))
    key4 = np.random.randint(0, 10, size = (9, 9))
    key5 = np.random.randint(0, 10, size = (9, 9))

    return key1, key2, key3, key4, key5

key1, key2, key3, key4, key5 = generate_key()

def encrypt_mat(matrix, key):

    encryption = np.matmul(matrix, key)
    encryption = np.remainder(encryption, 255)

    return encryption

def decrypt_mat(encryption, key):

    inverse_key = Matrix(key).inv_mod(255)
    inverse_key = np.array(inverse_key)
    inverse_key = inverse_key.astype(float)

    decryption = np.matmul(encryption, inverse_key)
    decryption = np.remainder(decryption, 255).flatten()

    return decryption

#message = np.random.randint(0, 255, size = (9, 9))

#print(message)

#encrypted_message = encrypt_mat(message, key1)

#decrypted_message = decrypt_mat(encrypted_message, key1)

#decrypted_message = np.reshape(decrypted_message, (9, 9))

#print(decrypted_message)
#print(decrypted_message.shape)