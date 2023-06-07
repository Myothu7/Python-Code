mylist = ["green", "blue", "red", "cyan"]

#add an item to end function
def append(list,value): 
		addlist = [value]
		list += addlist
		return list

a = append(mylist,"gray")
print(a)
