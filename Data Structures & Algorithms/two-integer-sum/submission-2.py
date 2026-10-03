# Things learned:
# Careful what you access in hash tables, you were trying to acces indeces[4] for example which didn't exist yet instead of doing indeces[difference]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indeces:
                return [indeces[difference], i]
            else:
                indeces[n] = i
        return []

