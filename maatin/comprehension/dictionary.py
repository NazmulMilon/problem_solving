a_list = ['name', 'country', 'career']
b_list = ['Maateen', 'Bangladesh', 'TeleTalk']
my_dict = {i : j for i,j in zip(a_list, b_list)}
print(my_dict)


list1 = ['Name', 'Age', 'Salary']
list2 = ['Nazmul', '26', '50000']
dict = {i:j for i,j in zip(list1, list2)}
print(dict)