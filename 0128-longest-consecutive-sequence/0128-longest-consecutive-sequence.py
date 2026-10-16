class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        snums = sorted(list(set(nums)))
        maxy = 1
        maxx = 1
        for i in range(len(snums)-1):
            if snums[i] + 1 == snums[i+1]:
                maxy += 1
            else:
                maxx = max(maxx, maxy)
                maxy = 1
        return max(maxx, maxy)