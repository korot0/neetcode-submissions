class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indeces:
                return [indeces[difference], i]
            indeces[nums[i]] = i