

def is_even(n):
    return n%2==0


nums = [3, 2, 6, 8, 14, 16, 22, 9]

evens = list(filter(is_even, nums))

print(evens)