class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = s.lower().replace(" ", "")
        s = re.sub(r'[^A-Za-z0-9]', "", s)

        left = 0
        right = -1

        print(s)

        while left < len(s) + right +1:
            print(s[left], s[right])
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True
