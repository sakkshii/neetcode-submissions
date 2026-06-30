class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> store= new HashSet<>();

        for(int val: nums){
            store.add(val);
        }

        int res =0;

        for(int num: nums){
            int streak =0, curr = num;
            while(store.contains(curr)){
                streak++;
                curr++;
            }
            res = Math.max(res, streak);
        }
    return res;
    }
}
