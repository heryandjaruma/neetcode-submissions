class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        
        # strip space
        s = s.strip()
        # replace all spaces
        s = s.replace(" ", "")

        left = 0 
        right = -1
        
        while left < abs(right):
            print(f"L {left} {s[left]}  R {right} {s[right]}")
            
            while True:
                if s[left] in valid:
                    break
                else:
                    left += 1
            
            while True:
                if s[right] in valid:
                    break
                else:
                    right += 1
            
            if s[left].lower() == s[right].lower():
                left += 1 
                right -= 1
                continue
            else:
                return False
        return True

