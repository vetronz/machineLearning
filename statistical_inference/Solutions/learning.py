# possible solutions


# 1
img.shape
img.dtype
len(img.shape)
img.ndim

# 2
imageio.imwrite("~/Downloads/cat_slice.jpg", img[:200, :200, :])
imageio.imwrite("~/Downloads/cat_grey.jpg", img[:, :, 0])

# 3
imageio.imwrite("~/Downloads/cat_substract.jpg", img-img)
imageio.imwrite("~/Downloads/cat_substract_switched.jpg", img-img+255)
imageio.imwrite("~/Downloads/cat_sum.jpg", img+img)

# 4
%matplotlib notebook
import matplotlib.pyplot as plt
plt.imshow(np.uint8(img*[1,0.95,0.9]))

# 5
min_distance = 9999 # initialise a value for the distance
for i in range(0, X_train.shape[0]):
    distance = np.sum(np.abs(X_ursus[0,:,:,0]-X_train[i,:,:,0]))
    if distance < min_distance:
        min_distance = distance
        print("The closest image is " + labels[np.argmax(y_train[i])] + " with distance", distance)





