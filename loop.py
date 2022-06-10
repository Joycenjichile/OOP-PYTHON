thislist=["apple","banana","mango"]
for x in thislist:
   print(x)

thislist=["apple","banana","mango","cherry"]
for x in range(len(thislist)):
    print(thislist[x])   


thislist=["apple","mango","avocado","banana"] 
x=0
while x<len(thislist):
    print(thislist[x])
    x=x+1


fruits=["apple","mango","kiwi","cherry"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)     