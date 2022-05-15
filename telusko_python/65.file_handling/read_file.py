
f = open('sample.txt', 'r')
f_out = open('word_count.txt', 'w')
# print(f)
# print(f.read())

# print(f.readline(), end="#")
'''print(f.readline())'''
# print(f.readline()) # will print second line
# print(f.readline(5))


# print(f.readlines())

'''for line in f:
    print(line)
f.close()
'''

for line in f:
    token = line.split(' ')
    ##print(str(token))
    f_out.write("Wordcount: "+ str(len(token))+" "+ line)
    print(len(token))
f.close()