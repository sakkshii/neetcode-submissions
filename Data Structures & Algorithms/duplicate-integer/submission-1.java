class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashL= new HashSet<>();
        for(int val: nums){
            if(hashL.contains(val)){
                return true;
            }
            else{
                hashL.add(val);
            }
        }
    return false;
    }
}