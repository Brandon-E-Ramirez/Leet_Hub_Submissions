class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n) #populate 'ans' arr with 0's with twice the length of 'nums'
        
        for i in range(n):  #first half of the 'ans' arr is populated
            ans[i] = nums[i]
            
        for o in range(n):  #second half of array starts at length of original array 
            ans[n + o] = nums[o]
            
        return ans
    
    