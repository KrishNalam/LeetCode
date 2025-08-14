class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singular = set()
        for x in nums:
            singular.remove(x) if x in singular else singular.add(x)
        return singular.pop()