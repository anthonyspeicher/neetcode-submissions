class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}

        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1

        frequency = sorted(nums_map.values(), reverse=True)
        final = []

        for i in range(k):
            num = list(nums_map.keys())[list(nums_map.values()).index(frequency[i])]
            final.append(num)
            del nums_map[num]

        return final