class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        hmap = {}

        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num]+=1

        for num, freq in hmap.items():
            heapq.heappush(heap, (-freq,num))
        
        ls = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ls.append(num)

        return ls

        
        