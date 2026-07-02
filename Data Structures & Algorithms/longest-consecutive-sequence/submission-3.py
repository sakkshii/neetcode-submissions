class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        visited = set(nums)
        cnt = 1
        heap = []
        if len(nums) == 0:
            return 0
        for num in sorted(visited):
            val = num+1
            if val in visited:
                cnt+=1
            else:
                heapq.heappush(heap,-cnt)
                cnt = 1
        heapq.heappush(heap, -cnt)
        return - heapq.heappop(heap)


        