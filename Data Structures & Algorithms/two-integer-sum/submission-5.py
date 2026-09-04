class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            sub = target-nums[i]
            if hmap is None:
                hmap[sub] = i 
            else:
                if nums[i] in hmap:
                    return [hmap[nums[i]], i]
                else:
                    hmap[sub] = i


        