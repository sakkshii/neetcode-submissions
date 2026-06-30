class Solution {
    public int[] productExceptSelf(int[] nums) {
        int start =0;
        int res[]=new int[nums.length];
        while(start!=nums.length){
            int end=0;
            int prod=1;
            while(end!=nums.length){
                if(start==end){
                    end++;
                }
                else{
                    prod = prod*nums[end];
                    end++;
                }
            }
            res[start]=prod;
            start++;
        }
    return res; 
    }
}  
