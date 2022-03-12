
https://www.hackerrank.com/challenges/max-array-sum/forum
import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    len_array = len(arr)
    maxs_array = [0] * len_array

    for index in xrange(len_array):
        current_number = arr[index]

        prev_max_index = index - 2
        prev_prev_max_index = index - 3
        local_max_even = float('-INF')
        local_max_odd = float('-INF')

        if prev_max_index >= 0:
            prev_max_sum = maxs_array[prev_max_index]
            local_sum = current_number + prev_max_sum
            local_max_even = max(current_number, prev_max_sum, local_sum)
        if prev_prev_max_index >= 0:
            prev_max_sum = maxs_array[prev_prev_max_index]
            local_sum = current_number + prev_max_sum
            local_max_odd = max(current_number, prev_max_sum, local_sum)
        if prev_prev_max_index < 0 and prev_max_index < 0:
            local_max_even = current_number
        maxs_array[index] = max(local_max_even, local_max_odd)

    return max(maxs_array)


'''def maxSubsetSum(arr):
    dp = {} # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]


'''