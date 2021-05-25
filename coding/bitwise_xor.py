def find_missing_number(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i
    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]
    # missing number is the xor of x1 and x2
    return x1 ^ x2


def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_one = 1
    while (rightmost_one & n1xn2) == 0:
        rightmost_one = rightmost_one << 1
    num1 = 0
    num2 = 0
    for num in nums:
        if (num & rightmost_one) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


arr = [1, 5, 2, 6, 4] 
# print('Missing number is:' + str(find_missing_number(arr)))
res = find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])
print(res)

