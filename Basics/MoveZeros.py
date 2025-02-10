# MoveZeros.py

# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeros(nums) :
    zerosCount = 0

    while 0 in nums :
        nums.remove(0)
        zerosCount += 1

    while zerosCount > 0 :
        nums.append(0)
        zerosCount -= 1
    
    return nums

print(moveZeros([0,1,0,3,12]))

# Notes ::

# The remove operation in Python lists has a time complexity of O(n)
# Appending elements (nums.append(0)) takes O(1) time per operation.

# Thus,

# Worst-case time complexity: O(n²)
# Best-case time complexity: O(n) (if there are no zeros).
# Space complexity: O(1).

print("--------------------------")

# Better time complexity solution

def move_zeros(nums) :
    zeros_index = 0

    for i in range(len(nums)) :
        if nums[i] == 0 :
            continue
        elif nums[i] != 0 :
            nums[i] , nums[zeros_index] = nums[zeros_index] , nums[i]
            zeros_index += 1
    
    return nums

print(move_zeros([0,1,0,3,12]))