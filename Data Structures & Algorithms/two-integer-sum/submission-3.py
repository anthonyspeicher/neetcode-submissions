class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in nums_map:
                return [nums_map[remaining], i]
            nums_map[nums[i]] = i