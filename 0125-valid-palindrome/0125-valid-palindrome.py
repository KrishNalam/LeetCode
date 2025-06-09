class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            s = s.replace(i, "") if not i.isalnum() else s
        return s.lower() == s.lower()[::-1]