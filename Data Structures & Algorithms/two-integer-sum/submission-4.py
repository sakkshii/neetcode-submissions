class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}
        for i , num in enumerate(nums):
            val = target - num
            if val in visited:
                return [visited[val], i]
            else:
                visited[num] = i
        return [-1,-1]

        
      



            

            

                
        