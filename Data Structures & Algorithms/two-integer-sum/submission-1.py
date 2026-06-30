class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map= {}
        for i in range(len(nums)):
            val= target-nums[i]
            if val in Map:
                idx= Map[val]
                return [idx, i]
            else:
                Map[nums[i]]=i
        return [-1,-1]          

            

            

                
        