class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        output = 0
        for i in range(len(s)):
            output += trans[s[i]]
            if i+1 < len(s):
                if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    output -= 2
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    output -= 20
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"): 
                    output -= 200
        return output