lst = []
n = int(input("Enter the range of list: "))

lst = list(map(int, input(" Enter number: ").split()))[:n]
# lst = list(map(int, input("Enter the elements: ").strip().split()))[:-n]
print(lst)


''''# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", a)
'''
