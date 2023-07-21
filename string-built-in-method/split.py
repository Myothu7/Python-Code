text = "hello Myo Min Thu how are you?"


def split_test(txt):
    txt_list = []
    index = []
    for i in range(len(txt)):
        if txt[i] == " ":
            index.append(i)
    n = len(index)
    txt_list.append(txt[0:index[0]])
    for i in range(n - 1):
        txt_list.append(txt[index[i]:index[i + 1]])  # 5,9 9
    txt_list.append(txt[index[-1]:])
    return txt_list


print(split_test(text))
