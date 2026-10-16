class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        final = []
        for i in nums:
            temp[i] = temp.get(i, 0) + 1
        mapping = sorted(list(temp.values()), reverse = True)[:k]
        for x in temp.keys():
            if temp[x] in mapping:
                final.append(x)
        return final
        