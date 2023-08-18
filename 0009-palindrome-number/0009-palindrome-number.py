class Solution:
    def isPalindrome(self, x: int) -> bool:
        #x is an integer, convert to string then process
        xStr = str(x);
        revXStr = xStr[::-1];
        if(xStr == revXStr):
            return True;
        elif (xStr != revXStr):
            return False;