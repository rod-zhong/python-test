filename='programming.txt'
"""
1. 当文件不存在的时候会自动创建。
2. 文件的模式有三种 
    (r: 只读模式、默认的模式当没有提供参数的时候）: r means readonly
    (w: 写入模式、当文件已存在的时候会覆盖所有内容) : w means write
    (a:追加模式。在文件中追加内容) : a means append
"""
def __init__():
    with open(filename,"w") as file_object:
        print("clean file data")
    

def writeOneLine():
    with open(filename,'w') as file_object:
        file_object.write("I love programming.\n")
def writeMultipleLines():
    with open(filename,'a') as file_object:
        for x in range(3):
            file_object.write("You will see multiple data \n")
def readFile():
    with open(filename,"r") as file_object:
        for x in file_object.readlines():
            print("read data is :",x)

__init__()

print("start write sth into file for test")
writeOneLine()
writeMultipleLines()
print("read file again to see what been changed")
readFile()