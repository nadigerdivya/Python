# TwoSum.py

# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=plakya4j

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(list, target) :
    map = {}
    for num in range(0, len(list)) :
        cur = list[num]
        diff = target - cur
        if diff in map :
            return [map[diff], num]
        else :
            map[cur] = num

list = [2,7,11,15]
target = 9
print(twoSum(list, target))