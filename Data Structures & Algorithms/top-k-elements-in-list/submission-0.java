class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map= new HashMap<>();

        for(int val: nums){
            if(!map.containsKey(val)){
                map.put(val, 1);
            }
            else{
                int currentCount = map.get(val);
                currentCount++;
                map.put(val, currentCount);
            }
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());

        Collections.sort(list, (a,b) -> b.getValue()-a.getValue());

        int [] res = new int[k];

        for(int i=0; i<k; i++){
            res[i] = list.get(i).getKey();
        }

    return res; 
    }
}
