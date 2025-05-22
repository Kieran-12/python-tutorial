lst_main = []
lst_sub = []
lst_sub = eval(input())
print(f"lst_sub={lst_sub}")


def transpose(lst):
    result = []
    h = len(lst)
    w = len(lst[0])
    for y in range(w):
        print(y)
        result.append([])
        for x in range(h):
            print(x)
            result[y].append(lst[x][y])
    return result


lst = [[1, 2], [4, 5], [7, 8]]
x = transpose(lst)

print(x)
