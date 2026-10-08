class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [0] * 2
        n = len(numbers)

        left = 0
        right = n - 1
        for i in range(n):
            if numbers[left] + numbers[right] == target:
                res[0], res[1] = left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return res