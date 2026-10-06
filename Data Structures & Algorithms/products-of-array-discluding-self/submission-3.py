class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        o = [0] * nums_length
        p = [0] * nums_length
        s = [0] * nums_length

        p[0] = s[nums_length - 1] = 1

        for i in range(1, nums_length):
            p[i] = nums[i - 1] * p[i - 1]
        for i in range(nums_length - 2, -1, -1):
            s[i] = nums[i + 1] * s[i + 1]
        for i in range(nums_length):
            o[i] = p[i] * s[i]

        return o

# Instead of appending to the arrays, we could initialize them with nums_length elements and assign values by index.. avoiding having to manage the negative indices.