class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> elements = new HashSet<>();
        int duplicates = 0;

        for(int i = 0; i < nums.length; i++){
            if(elements.contains(nums[i])){
                elements.add(nums[i]);
                duplicates++;
            }else{
                elements.add(nums[i]);
            }
        }

        if(duplicates > 0){
            return true;
        }else{
            return false;
        }
    }
}