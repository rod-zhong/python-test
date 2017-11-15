#!usr/bin/env python3

def read_file(file_path):
    f = None
    try:
        f = open(file_path,"r")
        print(f.read())
    except IOError as e:
        print("can't open file",e)
    finally:
        print("execute finally")
        if f is not None:
            f.close()
            print("execute close ")

def read_file2(file_path):
    with open(file_path,"r") as f:
        while f.readline() is not None:
            print("xxx")

read_file("/tmp/test.txt")
read_file2("/tmp/test.txt")