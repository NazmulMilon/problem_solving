

s1 = input()
s2=input()

str1 = s1.lower()
str2 = s2.lower()
len1 = len(str1)
len2 = len(str2)

if len1 ==len2:
    if str1>str2:
        print("1")
    elif str1<str2:
        print("-1")
    else:
        print("0")