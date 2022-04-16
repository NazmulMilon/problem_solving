

'''n = input()
line = input()

str1 = line.find("1") == -1 and "EASY" or "HARD"
print(str1)'''


n = int(input())
line = []

for i in range(n):
    a=int(input())
    line.append(a)

for j in range(len(line)):
    if line[j]==1:
        print("HARD")
        break
else:
    print("EASY")

