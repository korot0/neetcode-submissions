class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        o = []
        p = [1]
        s = [1]
        s_index = 1

        for i in range(1, nums_length):
            p.append(nums[i - 1] * p[i - 1])
        
        for i in range(nums_length - 2, -1, -1):
            s.append(nums[i + 1] * s[s_index - 1])
            s_index += 1

        p_index = 0
        s_index = -1
        for i in range(nums_length):
            o.append(p[p_index + i] * s[s_index - i])  

        return o