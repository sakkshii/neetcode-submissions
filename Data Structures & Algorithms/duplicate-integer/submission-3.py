class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if num in visited:
                visited[num] += 1
                return True
            else:
                visited[num] = 1
        return False