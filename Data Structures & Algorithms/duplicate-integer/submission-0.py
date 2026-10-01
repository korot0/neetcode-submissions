class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for item in nums:
            if item in data:
                return True
            else:
                data.add(item)
        return False