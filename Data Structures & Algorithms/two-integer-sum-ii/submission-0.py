class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1

        while True:
            sum = numbers[first] + numbers[last]
            if sum == target:
                return [first + 1, last + 1]
            
            if sum < target:
                first += 1
            else:
                last -= 1