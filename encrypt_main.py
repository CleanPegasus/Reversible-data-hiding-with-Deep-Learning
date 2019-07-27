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

data_bit = []

for i in range(data.shape[1]):

    data_bit.append(bin(int(data[0, i])))

#print(data_bit)

key1, key2, key3, key4, key5 = generate_key()


img = cv2.imread('image.jpg', 0)

cv2.imwrite("Original.jpg", img)

encrypted_image = np.zeros(shape = (img.shape[0], img.shape[1]))

for i in range(int(img.shape[0] / 9)):

    if(i < len(data_bit)):

        embedding_bit = data_bit[i]

        #print(len(embedding_bit))

    for j in range(int(img.shape[1] / 9)):

        if(j < len(embedding_bit)):

            if(embedding_bit[j] == 0):
                key = key1
            if(embedding_bit[j] == 1):
                key = key2
            if(embedding_bit[j] == "b"):
                key = key3
            if(embedding_bit[j] == "-"):
                key = key4
        
        else:
            key = key5
    

        blob = img[i * 9 :  (i + 1) * 9, j * 9 : (j + 1) * 9]

        encrypted_blob = encrypt_mat(blob, key1)

        encrypted_image[i * 9 :  (i + 1) * 9, j * 9 : (j + 1) * 9] = encrypted_blob


cv2.imwrite("encrypted_image.jpg", encrypted_image)
        
