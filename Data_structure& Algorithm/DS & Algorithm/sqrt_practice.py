def sqrt(num):
    low = 0
    high = num

    while high - low > 0.0001:
        mid = (high + low) / 2
        if mid * mid > num:
            high = mid
        else:
            low = mid
    return mid


print(sqrt(25))