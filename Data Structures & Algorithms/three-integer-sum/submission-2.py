class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                triplet = nums[i] + nums[left] + nums[right]
                if triplet == 0:
                    indeces = [nums[i], nums[left], nums[right]]
                    if indeces not in res:
                        res.append(indeces)
                    left += 1
                elif triplet < 0:
                    left += 1
                else:
                    right -= 1

        return res
        