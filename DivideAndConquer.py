
import math
import random


def hanoi_and_count(n, A, B, C):
    if n == 1:
        C.append(A.pop())
        return 1
    else:
        return hanoi_and_count(n - 1, A, C, B) + hanoi_and_count(1, A, B, C) + hanoi_and_count(n - 1, B, A, C)


def MinMax(A, i, j):
    if i == j:
        return (A[i], A[j])
    if j == i + 1:
        return (min(A[i], A[j]), max(A[i], A[j]))
    res1 = MinMax(A, i, (i + j) // 2)
    res2 = MinMax(A, (i + j) // 2 + 1, j)
    return (min(res1[0], res2[0]), max(res1[1], res2[1]))


def longest_common_prefix(str_arr, s, e):
    if s == e:
        return str_arr[s]
    mid = (s + e) // 2
    res1 = longest_common_prefix(str_arr, s, mid)
    res2 = longest_common_prefix(str_arr, mid + 1, e)
    return longest_common_prefix_for_two(res1, res2)


def longest_common_prefix_for_two(str1, str2):
    res = ''
    for i, char in enumerate(str1):
        if i >= len(str2) or not char == str2[i]:
            return res
        res += char
    return res


def MaxCrossSum(arr, mid):
    sum = 0
    left_sum = rigth_sum = None
    for i in range(mid, len(arr)):
        sum += arr[i]
        if rigth_sum == None or rigth_sum < sum: rigth_sum = sum
    sum = 0
    for i in range(mid + 1):
        sum += arr[i]
        if left_sum == None or left_sum < sum: left_sum = sum

    return max(rigth_sum, left_sum, rigth_sum + left_sum - arr[mid])


def maxSum(arr):
    if len(arr) == 1: return arr[0]
    mid = len(arr) // 2
    lMax = maxSum(arr[:mid])
    mMax = MaxCrossSum(arr, mid)
    rMax = maxSum(arr[mid:])
    return max(lMax, mMax, rMax)


def median(arr, pivot_fn=random.choice):  # quick select algorithm
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(arr, len(arr) / 2, pivot_fn) + quickselect(arr, len(arr) / 2 - 1, pivot_fn))


def quickselect(arr, nth_element, pivot_fn):
    if len(arr) == 1:
        assert nth_element == 0
        return arr[0]
    pivot = pivot_fn(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if nth_element < len(lows):
        return quickselect(lows,nth_element,pivot_fn)
    if nth_element < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs,nth_element - len(lows) - len(pivots),pivot_fn)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [19, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
    print(median(arr))
