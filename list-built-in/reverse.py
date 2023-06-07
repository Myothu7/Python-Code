mylist = ["apple", "banana", "mango", "cherry"]

def reverse(list):
	k = len(list) - 1
	mylist = []
	for a in range(k,-1,-1):
		mylist += [list[a]]
	return mylist

list = reverse(mylist)
print(list)

