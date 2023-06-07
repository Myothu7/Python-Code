mylist = ["green", "blue", "red", "cyan"]

def index(list,value):
	for x in range(len(list)):
		for a in list:
			if(a == list[x] and value == list[x]):
				return x
		
x = index(mylist,"green")
print(x)
