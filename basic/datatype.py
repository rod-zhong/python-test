#!/usr/bin/env python3

"""
  Lean how to use dictionary object. add/update/delete/loop/copy/etc..
  tuple / list / set 三者的主要区别和主要创建模式为
  my_tuple = (1,2,3) #不可变
  my_list = [1,2,3]  #可变
  my_set = {1,2,3}   #可变
"""
def testDict():
    """
      What is dict, how to use dict, why need use dict
    """
    mydict = {"key1":"value1","key2":[1,2,3]}
    print('how to know the data is which type',type(mydict))  #know the type 
    if "key3" in mydict:
      print("i am going to retrive the value for key3",mydict['key3'])
    val2 = mydict["key1"]  #get value use another way 
    print('value of key1 is',val2)

    #loop keys and get the value via 
    for x in mydict:
        print('{',x,' : ',mydict[x],'}')

    for x,y in mydict.items():
        print('xxxx',x,y)


testDict()




