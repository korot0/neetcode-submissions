class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums_set = set(nums)
        seen = set()

        longest = 0
        temp = 1

        right = 1
        left = -1

        for i in range(nums_length):
            current = nums[i]
            seen.add(current)

            while True:
                if (current + right) in nums_set and (current + right) not in seen:
                    seen.add(current + right)
                    temp += 1
                    right += 1
                else:
                    break

            while True:
                if (current + left) in nums_set and (current + left) not in seen:
                    seen.add(current + left)
                    temp += 1
                    left -= 1
                else:
                    break

            if temp > longest:
                longest = temp
            temp = 1
            right = 1
            left = -1

        return longest