from Greedy import Item


def fibonacci(n):
    array = [1, 1]
    if n <= 2:
        return array[0]
    i = 0
    while i < n - 2:
        array.append(array[i] + array[i + 1])
        i += 1
    return array.pop()


def knapsack(items, sacksize):  # O(n) Pseudopolynomial -> sacksize*len(items), where sacksize its a number
    table = [[0 for j in range(sacksize + 1)] for i in range(len(items) + 1)]
    for i in range(len(items) + 1):
        for j in range(sacksize + 1):
            if not i == 0:  # because first line its empty sack so its always 0 value
                item = items[i - 1]
                dont_take = table[i - 1][j]
                take = 0
                if j - item.weight >= 0: take = table[i - 1][j - item.weight] + item.price
                table[i][j] = max(take, dont_take)
    print_table(table)
    return table[len(items)][sacksize]


def print_table(table):
    print('\n'.join(' '.join(str(x) for x in row) for row in table))


def kadane(arr):  # max sub array  O(n)
    temp_arr = [0 for i in range(len(arr))]
    if arr[0] > 0: temp_arr[0] = arr[0]
    for i in range(1, len(arr)):
        sum = temp_arr[i - 1] + arr[i]
        if sum < 0: sum = 0
        temp_arr[i] = sum
    return max(temp_arr)


def kadane_matrix(mat):  # max sub matrix O(nˆ3)
    width = len(mat[0])
    height = len(mat)
    max_sum = None
    for k in range(height):
        help_arr = [0 for x in range(height)]
        for i in range(k, height):
            for j in range(width):
                help_arr[i] += mat[i][j]
                cur_sum = kadane(help_arr)
                if max_sum is None or cur_sum > max_sum:
                    max_sum = cur_sum
    return max_sum


def LCS(str1, str2): # longest common str O(nm)
    width = len(str1) + 1
    height = len(str2) + 1
    mat = [[0 for j in range(width)] for i in range(height)]
    for i in range(1,height):
        for j in range(1,width):
            if str2[i - 1] == str1[j - 1]: mat[i][j] = 1 + mat[i-1][j-1]
            else: mat[i][j] = max(mat[i-1][j],mat[i][j-1])
    res = ''
    i = height-1
    j = width-1
    while mat[i][j]:
        if str1[j-1] == str2[i-1]:
            res = str1[j-1] + res
            i-=1
            j-=1
        else:
            if mat[i-1][j] >= mat[i][j-1]: i-=1
            else: j-=1

    return res

def is_subset_sum(nums, sum):  # O(nm) -> n = len(nums) m = sum pseudopolinomial
    width = sum
    height = len(nums) + 1
    mat = [[False for j in range(width)] for i in range(height)]
    for i in range(height):
        mat[i][0] = True

    for i in range(1,height):
        for j in range(1,width):
            if nums[i-1] <= j:
                mat[i][j] = mat[i-1][j] or mat[i-1][j - nums[i-1]]
            else:
                mat[i][j] = mat[i-1][j]

    return mat[height-1][width-1]

def num_of_actions(from_str,to_str):  # return number of actions to do to create new string from old O(nm)
    width = len(from_str) + 1
    height = len(to_str) + 1
    mat = [[0 for j in range(width)] for i in range(height)]

    for i in range(height): mat[i][0] = i
    for j in range(width): mat[0][j] = j

    for i in range(1,height):
        for j in range(1,width):
            if from_str[j - 1] == to_str[i - 1]: mat[i][j] = mat[i-1][j-1]
            else:
                delete = mat[i][j-1]
                replace = mat[i-1][j-1]
                insert = mat[i-1][j]
                mat[i][j] = 1 + min(delete,replace,insert)
    return mat[height-1][width-1]


if __name__ == '__main__':
    mat = [[2, 1, -3, -4, 5],
           [0, 6, 3, 4, 1],
           [2, -2, -1, 4, -5],
           [-3, 3, 1, 0, 3]]
    print(num_of_actions('Sunday','Saturday'))
