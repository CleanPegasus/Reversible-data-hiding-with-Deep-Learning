from keras.models import load_model
import numpy as numpy
from keras.datasets import mnist
import matplotlib.pyplot as plt
import cv2

(X_train, y_train), (X_test, y_test) = mnist.load_data()

encoder = load_model('encoder.h5')
#encoder.compile(loss = 'mse', optimizer = 'Adam')

sample = X_test[1]
sample = sample.reshape([-1, 28, 28, 1])

data = encoder.predict_on_batch(sample)

decoder = load_model('decoder.h5')
decoder.compile(loss = 'mse', optimizer = 'Adam')

#data = data.reshape[-1, 16]

image = decoder.predict_on_batch(data)

#print(image[0])

cv2.imshow('image', image[0])
cv2.waitKey(0)