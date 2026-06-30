class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> hashL= new ArrayList<>();
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