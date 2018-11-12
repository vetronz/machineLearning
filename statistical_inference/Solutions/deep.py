

import numpy as np
import matplotlib.pyplot as plt
import keras

X_train = np.load("Data/X_train.npy")
y_train = np.load("Data/y_train.npy")

X_test = np.load("Data/X_test.npy")
y_test = np.load("Data/y_test.npy")

X_ursus = np.load("Data/X_ursus.npy")

# attempt 1

model = keras.Sequential()
model.add(keras.layers.Conv2D(filters=8, kernel_size=(3,3), strides=(1,1), activation="relu", padding="same", input_shape=(64, 64, 1)))
model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(keras.layers.Dropout(rate=0.5))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(units=32, activation="relu"))
model.add(keras.layers.Dense(units=4, activation="softmax"))

model.compile(optimizer=tf.train.AdamOptimizer(0.001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=10, validation_split=0.20)

score = model.evaluate(X_test, y_test)
print(score)








