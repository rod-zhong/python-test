filename='programming.txt'
"""
1. 当文件不存在的时候会自动创建。
2. 文件的模式有三种 
    (r: 只读模式、默认的模式当没有提供参数的时候）: r means readonly
    (w: 写入模式、当文件已存在的时候会*覆盖**覆盖**覆盖*所有内容) : w means write
    (a:追加模式。在文件中追加内容) : a means append
"""
def __init__():
    with open(filename,"w") as file_object:
        file_object.write("init file content as hellow world")
        print("clean file data")
    

def write_one_line():
    with open(filename,'w') as file_object:
        file_object.write("I love programming.\n")

def write_multiple_lines():
    with open(filename,'a') as file_object:
        for x in range(3):
            file_object.write("You will see multiple data \n")  # '\n' you know what i mean, new line 

def read_from_file(algo='other'):                  # defaut variable 
    with open(filename,"r") as file_object:
        if algo == 'byline':
            for line in file_object.readlines():
                print("read data is :", line.strip())  # strip() removed EOF and blank string
        else:
            content = file_object.read()     # read() return entire file content, not good for large file 
            print(content.strip())
__init__()
read_from_file()
print("start write sth into file for test")
write_one_line()
write_multiple_lines()
print("read file again to see what been changed")
read_from_file("byline")