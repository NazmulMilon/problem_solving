

# f1 = open('new_file', 'w')
# f1.write("Laptop")
# f1.write('Something')

f = open('sample.txt', 'r')
f1 = open('new_file', 'a')
# f1.write('Mobile')

for data in f:
    f1.write(data)

# for data in f:
    # print(data)




