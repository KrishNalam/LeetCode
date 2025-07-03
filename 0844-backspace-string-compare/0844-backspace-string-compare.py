class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lsts, lstt = [], []
        for i in s:
            if i == "#" and lsts:
                lsts.pop()
            elif i != "#":
                lsts.append(i)
        for i in t:
            if i == "#" and lstt:
                lstt.pop()
            elif i != "#":
                lstt.append(i)
        return lsts == lstt