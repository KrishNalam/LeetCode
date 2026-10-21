class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums)-1
        mid = r//2
        if nums[0] <= nums[r]:
            return nums[0]
        while nums[mid] < nums[mid + 1]:
            if nums[mid] < nums[r]:
                r = mid
                mid = mid//2
            elif nums[0] < nums[mid]:
                mid = (mid + r)//2
        return nums[mid+1]