txt = "Good programmers write code that humans can understand"

def find(txt,str):
    for i in range(len(txt)):
        if txt[i:i+len(str)] == str:
            return i

def replace(txt,value,chvalue):
    length = len(value)
    index = find(txt,value)
    return txt[0:index]+chvalue+txt[index+length:]

newstr = replace(txt,'programmers','developer')
print(newstr)