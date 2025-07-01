class Solution:
    def longestPalindrome(self, s: str) -> int:
        counters = {}
        for x in s:
            if x in counters.keys():
                counters[x] += 1
            else:
                counters.update({x:1})
        output = 0
        single = True
        lst = list(counters.values())
        for x in lst:
            if x%2 == 0:
                output += x
            elif(x-1) != 0:
                output += x-1
                lst.append(1)
            elif single:
                output += 1
                single = False
        return output