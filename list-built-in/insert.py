mylist = ["green", "blue", "red", "cyan"]

def insert(list, key, value):
	result = list[0:key] + [value] +list[key:]
	return result
	
print("List: " ,mylist)	 
mylist = insert(mylist,1,"black")
print("Insert list:" ,mylist)

print(mylist[0:])