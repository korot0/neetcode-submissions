class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        countNums = defaultdict(int)
        heap = []

        for num in nums:
            countNums[num] += 1

        for num in countNums.keys():
            heapq.heappush(heap, (countNums[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res