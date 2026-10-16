class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = {}
        right = {}
        out = []
        count = 1
        for i in range(len(nums)):
            count *= nums[len(nums)-1-i]
            right[len(nums)-i-1] = count
        right[len(nums)] = 1
        count = 1
        out.append(right[1])
        for i in range(1, len(nums)):
            count *= nums[i-1]
            out.append(count*right[i+1])
        return out