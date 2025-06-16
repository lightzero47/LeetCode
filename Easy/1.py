def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        pair = target - num
        if pair in num_to_index:
            return [num_to_index[pair], i]
        num_to_index[num] = i
    return []

print(two_sum([2,7,11,15], 9)) 
print(two_sum([3,2,4], 6))      
print(two_sum([3,3], 6))       