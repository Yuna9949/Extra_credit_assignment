def targetSum(array, target_sum):
    a = 0
    b = 1
    while True:
        print("a = "+ str(a) +", b = " + str(b))
        if array[a] + array[b] == target_sum:
            return [array[a], array[b]]
        b = b + 1
        if b == len(array):
            a = a + 1
            b = a + 1
        if a == len(array) - 1:
            return [0, 0]

print(targetSum([2, 7, 11, 15], 9))