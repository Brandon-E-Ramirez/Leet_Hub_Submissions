class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n*2];
        //if n = 3, ans.length = 6
        //if n = 2, ans.length = 4
        
        for(int i = 0; i < n; i++){
            ans[i] = nums[i];
        }

        for(int i = 0; i < n; i++){
            ans[i+n] = nums[i];
        }
        return ans;
    }
}