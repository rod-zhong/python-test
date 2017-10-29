myList = ['A','B','C','D']
print(myList)

# loop each item
for item in myList:
    item += '1';
    print("this is for each to print each item", item,)
print(myList)

myList.insert(0,"1")
myList.append("E")
print(myList)

del myList[0]
print(myList)

# pop
inx = 0
while inx < 5:
    print(myList.pop())
    inx+=1
#end
