class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        actual = len(magazine)
        for x in ransomNote:
            magazine = magazine.replace(x, "", 1)
            actual -= 1
            if len(magazine) != actual:
                return False
        return True