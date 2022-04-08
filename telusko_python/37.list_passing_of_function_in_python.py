
def count_fn(lst):
    even = 0
    odd =0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd


lst = [14, 25, 44, 57, 23, 49, 90, 67, 54]


even, odd = count_fn(lst)
print(f"Even: {even}, Odd: {odd}")
