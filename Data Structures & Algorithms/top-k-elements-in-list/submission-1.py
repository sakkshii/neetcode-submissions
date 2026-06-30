class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num]=0
            cnt[num]+=1
        
        heap = []
        for num, freq in cnt.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res
        
