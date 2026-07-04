import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        first = 0
        last = len(s) - 1

        while (first < last):
            if s[first] != s[last]:
                return False

            # update pointers
            first += 1  
            last -= 1
        
        return True