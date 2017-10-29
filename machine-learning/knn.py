from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

#define input data/trainning data
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    label = ['A','A','B','B']
    return group,label
'''
group,label = createDataSet();

print(group)
print(type(label))
'''
fig = plt.figure()
ax = fig.add_subplot(111)

