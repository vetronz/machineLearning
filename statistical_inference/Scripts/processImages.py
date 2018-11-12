
import numpy as np
import os

import shutil

import keras

import tensorflow

from keras.utils import np_utils #Utilities that help in the data transformation
from keras import backend as K
K.set_image_dim_ordering('tf')
K.set_image_data_format('channels_last') #tensorflow

from PIL import Image

from sklearn.utils import shuffle

from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

path_resized = "Images_resized/"

img_rows = 64
img_cols = 64

LABELS = ["LC", "VU", "EN", "CR"]
NITER = 400 # for each class

im_matrix_rows = len(LABELS)*NITER
im_matrix_cols = img_rows*img_cols
im_matrix = np.empty((im_matrix_rows, im_matrix_cols), dtype='float32')
index = 0


listing = os.listdir(path_resized)

index = 0
for L in LABELS:
    prefix = "img.."+str(L)+".."
    # Flattening of each image and creation of im_matrix, the array that contains all IMAGES
    for i, im in enumerate(listing):
        if prefix in listing[i]:
           image = np.asarray(Image.open(path_resized + im)).flatten()
           image = image.astype('float32')
           im_matrix[index,:] = image
           index += 1

len(listing)

label = np.zeros((len(listing),), dtype=int)
start = 0
stop = NITER
for i in range(len(LABELS)):
    label[start:stop] = i
    start = start + NITER
    stop = stop + NITER

len(label)

im_matrix, label = shuffle(im_matrix, label, random_state=2)

X_train, X_test, y_train, y_test = train_test_split(im_matrix, label, test_size=0.25, random_state=4)

CHANNELS = 1

X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, CHANNELS)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, CHANNELS)

X_train /= 255
X_test /= 255

y_train = np_utils.to_categorical(y_train, len(LABELS))
y_test = np_utils.to_categorical(y_test, len(LABELS))


path_data = "../Data/"

np.save(path_data+"X_train", X_train, allow_pickle=False)
np.save(path_data+"X_test", X_test, allow_pickle=False)
np.save(path_data+"y_train", y_train, allow_pickle=False)
np.save(path_data+"y_test", y_test, allow_pickle=False)


path_test = "img..TEST..1.bmp"

image = np.asarray(Image.open(path_test)).flatten()
image = image.astype('float32')

im_matrix_rows = len(LABELS)*1
im_matrix_cols = img_rows*img_cols
im_matrix = np.empty((im_matrix_rows, im_matrix_cols), dtype='float32')
im_matrix[1,:] = image

X_ursus = image.reshape(1, img_rows, img_cols, CHANNELS)
X_ursus /= 255

#Y_test = net.predict(X_test, batch_size=None, verbose=1)
#y_test = np.argmax(Y_test, axis=1)

print(X_ursus.shape)

np.save(path_data+"X_ursus", X_ursus, allow_pickle=False)









