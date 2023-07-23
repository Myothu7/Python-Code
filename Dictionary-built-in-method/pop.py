car = {"brand": "Ford", "model": "Mustang", "year": 1964}


def pop(dict, key):
    result = {}
    for i in dict:
        if i == key:
            continue
        result[i] = dict[i]
    return result

a = pop(car, "year")
print(a)