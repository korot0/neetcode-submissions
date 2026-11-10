class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        n = len(nums)
        
        for i in range(n):
            goal = target - nums[i]
            if goal in ht:
                return [ht[goal], i]
            ht[nums[i]] = i
