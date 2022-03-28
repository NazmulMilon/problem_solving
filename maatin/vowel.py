print('please, input an alphabet:')
a = input()
if character >= 'a' and character <='Z' or character >='A' and character <="Z":
    if character in 'aeiouAEIOU':
        print('Vowel')
    else:
        print("Consonant")
else:
    print("Nothing")