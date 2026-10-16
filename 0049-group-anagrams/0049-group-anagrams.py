class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            index = "".join(sorted(list(i)))
            if index in temp.keys():
                temp[index].append(i)
            else:
                temp[index] = [i]
        return list(temp.values())