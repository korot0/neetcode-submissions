# Hardest problem yet imo because of ignoring duplicates
# In two pointers problems make sure to move left or right indeces accordingly if they repeat!

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                triplet = nums[i] + nums[left] + nums[right]
                if triplet == 0:
                    indeces = [nums[i], nums[left], nums[right]]
                    res.append(indeces)
                    left += 1
                    while left < right:
                        if nums[left - 1] == nums[left]:
                            left += 1
                        else:
                            break
                    while left < right:
                        if nums[right] == nums[right - 1]:
                            right -= 1
                        else:
                            break
                elif triplet < 0:
                    left += 1
                else:
                    right -= 1

        return res
        