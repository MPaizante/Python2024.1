def sublist(x):
    y = 0
    s = []
    while y < len(x):
        if x[y] == 5:
            break
        else:
            s.append(x[y])
        y += 1
    return s

def check_nums(x):
    y = 0
    s = []
    while y < len(x):
        if x[y] == 7:
            break
        else:
            s.append(x[y])
        y += 1
    return s

def sublistx(input_list):
    result = []
    index = 0

    while index < len(input_list) and input_list[index] != "STOP":
        result.append(input_list[index])
        index += 1

    return result


def stop_at_z(x):
    res = []
    i = 0
    while i < len(x) and x[i] != 'z':
        res.append(x[i])
        i += 1
    return res
sum2 = 0

lst = [65, 78, 21, 33]
x = 0
while x <len(lst):
    sum2 += lst[x]
    x += 1



def beginning(x):
    i = 0

    y = []
    while i < len(x) and x[i] != 'bye':
        if i < 10:
            y.append(x[i])
        i += 1
    return y

print(beginning("a b c de bye"))