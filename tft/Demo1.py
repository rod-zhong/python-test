import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_house = 160
np.random.seed(42)
house_size = np.random.randint(1000,3500,num_house)

np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(20000,70000,num_house)

plt.plot(house_size,house_price,"bx")
plt.xlabel("Size")
plt.ylabel("Price")
#plt.show()

def normalize(array):
    return (array - array.mean()) / array.std()

num_train_samples=math.floor(num_house * 0.7)
print(num_train_samples,type(num_train_samples))
#define training data

train_house_size = np.asarray(house_size[:num_train_samples])
train_house_price = np.asanyarray(house_price[:num_train_samples])

train_house_size_norm = normalize(train_house_size)
train_house_price_norm = normalize(train_house_price)

# define test data
test_house_size = np.array(house_size[num_train_samples:])
test_house_price = np.array(house_price[num_train_samples:])

test_house_size_norm = normalize(test_house_size)
test_house_price_norm = normalize(test_house_price)

# define place holder which used in tensorflow as variable pass into graph
tf_house_size = tf.placeholder("float",name="house_size")
tf_price = tf.placeholder("float",name="price")

print("here!")


