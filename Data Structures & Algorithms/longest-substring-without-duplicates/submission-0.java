class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLen=0;

        for(int i=0; i<n; i++){
            HashSet<Character> hash= new HashSet<>();
            int len=0;
            for(int j=i;j<n;j++){
                char ch=s.charAt(j);
                if(!hash.contains(ch)){
                    hash.add(ch);
                    len++;
                }else{
                    break;
                }
                
            }
        maxLen = Math.max(maxLen,len);
        }
    return maxLen;   
    }
}
