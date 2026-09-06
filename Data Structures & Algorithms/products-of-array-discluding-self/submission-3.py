class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = len(nums) * [1]

        pref = 1 
        for i in range(len(nums)):
            out[i] = pref 
            pref = pref * nums[i]

        suff = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = suff * out[i]
            suff = suff *nums[i]

        return out


        