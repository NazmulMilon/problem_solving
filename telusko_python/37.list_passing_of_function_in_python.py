
# assignment:: Take 10 names from user then count and display number of users who has length more than 5 letters.


def display(user_lst):
    count = 0
    not_count = 0
    for i in user_lst:
        if len(i)>5:
            count+=1


        else:
            not_count+=1

    return count


user_lst = ['milonn', 'nazmul', 'pk', 'mk', 'gk', 'roni', 'bayejid', 'rupol', 'net', 'sector']


c=display(user_lst)
print('More than 5 letters in word: ', c)



'''def count_fn(lst):
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
print(f"Even: {even}, Odd: {odd}")'''
