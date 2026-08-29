class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)

        return True

        