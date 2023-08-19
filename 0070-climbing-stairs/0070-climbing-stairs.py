class Solution:
    def climbStairs(self, n: int) -> int:
        #can increment by 1 or 2, how many ways can we do it with n elements?
        #1(1), 2([1,1],[2]), 3([1,1,1], [1,2], [2,1]), 4([1,1,1,1][1,1,2],[2,1,1],[1,2,1],[2,2])
        if(n == 1):
            return 1;
        elif (n ==2):
            return 2;
        
    
        permutations = [0 for i in range(n+1)]  #this array will need an empty index[0] to do code below
        permutations[1] = 1;
        permutations[2] = 2;
        for i in range(3, n+1):
            permutations[i] = permutations[i-1] + permutations[i-2];
        return permutations[n]
        