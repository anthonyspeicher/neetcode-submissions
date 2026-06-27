class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in nums_map:
                return [nums_map[remaining], i]
            nums_map[n] = i