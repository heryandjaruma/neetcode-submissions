class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = set(s)
        setT = set(t)

        # 1 first check for count
        # if not same, obv false
        if len(setS) != len(setT):
            return False
        
        # 2 check for char valid
        for char in setS:
            if char not in setT:
                return False
        return True