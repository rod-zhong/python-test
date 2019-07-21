#!usr/bin/env python3
import os

def write_file(file_path):

    f=[]

    try:
        if os.path.isfile(file_path)==False:
            os.mknod(file_path)
            print("created file for",file_path)
        f =open(file_path,"w")
        f.writelines("haha")
        print("write data to",file_path)
    except IOError as e:
        print("errors:", e)
    finally:
        if f:
            f.close()

write_file("/tmp/test.txt")