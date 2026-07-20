class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = {}
        setT = {}

        # build the set and char count
        for char in s:
            if char not in setS:
                setS[char] = 1
            else:
                setS[char] += 1
        for char in t:
            if char not in setT:
                setT[char] = 1
            else:
                setT[char] += 1

        # 1 first check for count
        # if not same, obv false
        if len(setS) != len(setT):
            return False
        
        # 2 check for char valid
        for char in setS:
            if char not in setT:
                return False
            else:
                if setS[char] != setT[char]:
                    return False
                    
        return True