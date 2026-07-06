class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []

        sp=0
        ep=len(numbers)-1
       
        while(sp<ep):
            sumN = numbers[sp]+numbers[ep]
            if(sumN > target):
                ep-=1 
            elif(sumN < target):
                sp+=1
            else:
                res.append(sp+1)
                res.append(ep+1)
                break
        return res

