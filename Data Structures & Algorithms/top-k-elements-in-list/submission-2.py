import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        pq = []
        res = []

        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        
        for key, value in frequencies.items():
            heapq.heappush_max(pq, (value, key))

        for i in range(k):
            res.append(heapq.heappop_max(pq)[1])
            
        return res

# Look into from collections import Counter. Basically a dictionary without the manual counting
# There is heappushpoop which could've been used to only keep < k elements in the list