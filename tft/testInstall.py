import tensorflow as tf
session = tf.Session()
a = tf.constant(1)
b=tf.constant(2)
print(session.run(a+b))


