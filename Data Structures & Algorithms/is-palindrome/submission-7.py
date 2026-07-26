class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        
        # strip space
        s = s.strip()
        # replace all spaces
        s = s.replace(" ", "")
        # allow alphanumeric only
        s = ''.join(char for char in s if char.isalnum())

        left = 0 
        right = len(s) - 1
        
        while left < right:
            print(f"L {left} {s[left]}  R {right} {s[right]}")
            
            while True:
                if s[left] in valid:
                    break
                elif (left + 1) >= right:
                    return False
                else:
                    left += 1
            
            while True:
                if s[right] in valid:
                    break
                elif (right - 1) <= left:
                    return False
                else:
                    right -= 1
            
            if s[left].lower() == s[right].lower():
                left += 1 
                right -= 1
                continue
            else:
                return False
        return True

