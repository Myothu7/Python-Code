mylist = ["green", "blue", "red", "cyan"]
otherlist = ["mango", "cherry", "pineapple"]

#append def
def append(list, value):
		list += [value]
		return list

#copy & clear def
def copy(ls):
    mylist =[]
    mylist += ls
    return mylist

def clear(list):
    val = list[0:0]
    return val

#extend def
def extend(ls,otherls):
    ls += otherls
    return ls

#insert def
def insert(list, key, value):
	result = list[0:key] + [value] +list[key:]
	return result

#length def
def count(mylist):
	len = 0
	for a in mylist:
		len += 1
	return len

#index def
def index(list,value):
	for x in range(len(list)):
		for a in list:
			if(a == list[x] and value == list[x]):
				return x

#pop & remove def
def pop(list,key):
    newlist = []
    for a in list:
        if(a != list[key]):
            newlist += [a]
    return newlist

def remove(list,value):
    newls = []
    for a in list:
        if(a != value):
            newls += [a] 
    return newls

#reverse def
def reverse(list):
	k = len(list) - 1
	newlist = []
	for a in range(k,-1,-1):
		newlist += [list[a]]
	return newlist

#call method

print("My List:",mylist ," Other List:", otherlist ,"\n")
#count
ls = count(mylist)
print("length:",ls)
#index
ls = index(mylist,"red")
print("index:",ls)
#copy
ls = copy(mylist)
print("copy:",ls)
#clear
ls = clear(mylist)
print("clear:",ls)
#insert
ls = insert(mylist,2,"Bob")
print("insert",ls)
#pop
ls = pop(mylist,2)
print("pop:",ls)
#remove
ls = remove(mylist,"green")
print("remove:",ls)
#reverse
ls = reverse(mylist)
print("reverse:",ls)
#append
ls = append(mylist, "black")
print("append:",ls)
#extend
ls = extend(mylist,otherlist)
print("extend:",ls)