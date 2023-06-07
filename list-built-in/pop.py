mylist = ["green", "blue", "red", "cyan"]

def pop(list,key):
    newlist = []
    for a in list:
        if(a != list[key]):
            newlist += [a]
    return newlist

print("Old List:", mylist)

mylist = pop(mylist,2) 
print("Remove list: ",mylist)