
lst = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

for i in range(0, len(lst)):
    for j in range(0, len(lst)-1):
        if lst[j]> lst[j+1] :
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

        print(lst)
    print()