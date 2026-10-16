class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        seen = []
        fin = 0
        while n < len(s):
            if s[n] in seen:
                ind = seen.index(s[n])
                seen = seen[ind+1:]
                seen.append(s[n])
            else:
                seen.append(s[n])
            n += 1
            fin = max(fin, len(seen))
        return fin