class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp1 = []
        temp2 = []
        for i in range(len(s)):
            temp1.append(s[i])
            temp2.append(t[i])
        return sorted(temp1) == sorted(temp2)