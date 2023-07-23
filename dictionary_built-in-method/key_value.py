student = {"name": "Myo Thu", "age": 21, "gender": "M"}


def keys(dictionary):
    key = []
    for i in dictionary:
        key.append(i)
    return key


def value(dictionary):
    value = []
    for i in dictionary:
        value.append(dictionary[i])
    return value

print(keys(student))
print(value(student))