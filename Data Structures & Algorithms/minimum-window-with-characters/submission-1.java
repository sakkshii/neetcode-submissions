class Solution {
    public String minWindow(String s, String t) {
        
        if(s==null || t==null || s.length()<t.length()){
            return "";
        }

        int[] map = new int[128];
        for(char ch: t.toCharArray()){
                map[ch]++;
        }
        int cnt= t.length();
        int right=0;
        int left=0;
        int startNode=0;
        int minLen=Integer.MAX_VALUE;

        while(right< s.length()){
            char ch = s.charAt(right);
            if(map[ch]>0){
                cnt--;
            }
            map[ch]--;
            right++;

            while(cnt==0){
                if(right-left < minLen){
                    minLen= right-left;
                    startNode= left;
                }
                char c =s.charAt(left);
                map[c]++;
                if(map[c]>0){
                    cnt++;
                }
                left++;
            }
        }
    return minLen == Integer.MAX_VALUE ? "" : s.substring(startNode, startNode + minLen);        
    }
}
