class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        tDict = {}
        
        for i in range(len(s)):
            #s[i] is a letter (key) and we are assigning it the number of occurrences 
            #from original string (value in dict)
            sDict[s[i]] = 1 + sDict.get(s[i], 0)    #'get' def avoids 'no key' error
            tDict[t[i]] = 1 + tDict.get(t[i], 0) 
        for n in sDict:
            if sDict[n] != tDict.get(n, 0):
                return False
            
        return True