import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        first = 0
        last = len(s) - 1

        while (first < last):
            if s[first].lower() != s[last].lower():
                return False

            # update pointers
            first += 1  
            last -= 1
        
        return True