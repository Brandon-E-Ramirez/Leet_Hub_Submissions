class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValMap = {} #hash map with {n(key), i(index/value)}

        for i, n in enumerate(nums):
            diff = target - n
            if(diff in prevValMap):
                return [prevValMap[diff], i]
            prevValMap[n] = i #add values to dict/hashmap with: "dictName[key] = value"

