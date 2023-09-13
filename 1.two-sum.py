#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# One pass solution O(N)
# Lookback hashmap technique - clever!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        res = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                res = [hmap[diff], i]
            hmap[num] = i
        return res

        
# @lc code=end