import cv2
import numpy as np
from test_encrypt import encrypt
from test_decrypt import decrypt
from encrypt_matrix import generate_key, encrypt_mat, decrypt_mat


from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot as plt


(X_train, y_train), (X_test, y_test) = mnist.load_data()

encoder = load_model('Autoencoders/encoder.h5')

sample = X_test[1]
sample = sample.reshape([-1, 28, 28, 1])

data = encoder.predict_on_batch(sample)


for i in range(data.shape[1]):

    data[0, i] = int(data[0, i])


key1, key2, key3 = generate_key()


fd = open("key.pem", "rb")
key = fd.read()
fd.close()

fd = open("iv.pem", "rb")
iv = fd.read()
fd.close()

img = cv2.imread('image.jpg', 0)


image = [] 

for i in range(int(img.shape[0] / 9)):
    

    for j in range(int(img.shape[1] / 9)):
        
        if

        blob = img[i * 9 :  (i + 1) * 9, j * 9 : (j + 1) * 9]

        encrypted_blob = encrypt_mat(blob, key1)

        image.append(encrypted_blob)

print(len(image))