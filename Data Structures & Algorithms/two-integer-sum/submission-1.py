class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}

        for i, n in enumerate(nums):
            indeces[n] = i;

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indeces and indeces[difference] != i:
                return[i, indeces[difference]]
        return []