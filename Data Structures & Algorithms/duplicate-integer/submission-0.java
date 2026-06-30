class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Arrays.sort(nums);
        // for(int i=0;i<nums.length-1;i++){
        //     if(nums[i]==nums[i+1] ){
        //         return true;
        //     }
        // }
        // return false;

        HashSet<Integer>set=new HashSet<>();

        for(int val:nums){
            if(set.contains(val)){
                return true;
            }
            set.add(val);
        }
        return false;
    }
}