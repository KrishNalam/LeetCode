class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)+1):
            if x >= len(nums) or x != nums[x]:
                return x