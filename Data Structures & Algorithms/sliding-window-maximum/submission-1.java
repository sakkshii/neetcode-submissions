class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {

        int ans[]=new int[(nums.length-k)+1];

        int right=0;
        

        while(right<(nums.length-k)+1){
            int left=right;
            int max=nums[right];
            int cnt=0;
            while(cnt<k){
                if(nums[left]>max){
                    max=nums[left];
                }
                cnt++;
                left++;
            }
            ans[right]=max;
            right++;
        }
        return ans;
    }
}
