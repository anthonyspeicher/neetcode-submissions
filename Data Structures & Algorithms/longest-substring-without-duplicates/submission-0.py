class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0

        for i in range(len(s)):
            current = set()
            for j in range(i, len(s)):
                if s[j] in current:
                    break
                
                current.add(s[j])

            maximum = max(maximum, len(current))

        return maximum