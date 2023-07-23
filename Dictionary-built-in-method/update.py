student = {"name": "Myo Thu", "age": 21, "gender": "M"}


def update(dict, update):
    for i in update:
        dict[i] = update[i]
    return dict

update(student, {"color": "red", 'class': 'A'})
print(student)
