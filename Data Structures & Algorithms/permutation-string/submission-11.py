class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        check1 = [0] * 26

        for i in s1:
            check1[ord(i) - ord('a')] = check1[ord(i) - ord('a')]+ 1

        l, r = 0, 0
        check2 =[0] * 26

        while r < len(s2):
            check2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if tuple(check2) == tuple(check1):
                    return True
                else:
                    check2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
            r += 1
        return False


