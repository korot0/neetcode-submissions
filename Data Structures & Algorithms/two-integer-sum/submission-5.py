class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            indeces = {}

            for i, n in enumerate(nums):
                diff = target - n
                if diff in indeces:
                    return [indeces[diff], i]
                indeces[n] = i