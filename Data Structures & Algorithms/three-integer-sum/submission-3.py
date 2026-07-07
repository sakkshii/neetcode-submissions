class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ZeroSet = set()

        for fp in range(len(nums)-2):
            sp = fp+1
            ep = len(nums) -1 

            while(sp<ep):
                tsum = nums[fp]+nums[sp]+nums[ep]
                if tsum == 0:
                    ZeroSet.add((nums[fp],nums[sp],nums[ep]))
                    sp+=1
                    ep-=1
                elif tsum < 0:
                    sp+=1
                else:
                    ep-=1
        return [list(ls) for ls in ZeroSet]



        