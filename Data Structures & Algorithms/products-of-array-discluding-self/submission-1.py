class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o = []
        p = [1]
        s = [1]
        s_index = 1

        for i in range(1, len(nums)):
            p.append(nums[i - 1] * p[i - 1])
        
        for i in range(len(nums) - 2, -1, -1):
            s.append(nums[i + 1] * s[s_index - 1])
            s_index += 1

        p_index = 0
        s_index = -1
        for i in range(len(nums)):
            o.append(p[p_index + i] * s[s_index - i])  

        return o