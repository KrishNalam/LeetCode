class Solution:
    def isValid(self, s: str) -> bool:
        final = []
        brackets = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in ["(", "{", "["]:
                final.append(c)
            elif final != []:
                if brackets[c] == final[-1]:
                    final.pop()
                else:
                    return False
            else:
                return False
        return final == []