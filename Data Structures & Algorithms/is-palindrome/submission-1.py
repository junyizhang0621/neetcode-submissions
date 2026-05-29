class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left <= right:
            lc = s[left]
            rc = s[right]

            if not lc.isalnum():
                left += 1
                continue
            
            if not rc.isalnum():
                right -= 1
                continue

            if lc != rc:
                return False
            left += 1
            right -= 1
        
        return True

        
        