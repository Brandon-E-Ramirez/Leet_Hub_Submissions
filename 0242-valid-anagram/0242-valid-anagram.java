class Solution {
    public boolean isAnagram(String s, String t) {
        //The two strings need to have the same total length (letters)
        int strLength = s.length();
        if(s.length() != t.length()){
            return false;
        }
        char[] charsS = s.toCharArray();
        char[] charsT = t.toCharArray();
        Arrays.sort(charsS);
        Arrays.sort(charsT);
    
        for(int i = 0; i < strLength; i++){
            if(charsS[i] != charsT[i]){
                return false;
            }
        }

        return true;

    }
}