class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = set()
         for n in nums
             #if n is in hashset, then they are duplicates.
             if n in hashset:
                 return True
             hashset.add(n)
        #if no n is in hashset, nothing is duplicate.
         return False
#tc: O(n)  sc:O(n)
________
#if brute force is used
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
         return False
#tc: O(n*n) sc: O(1)
________
#sort algorithm can be used, too.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         nums.sort()
         for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
         return False
#tc: O(nlogn)  sc: O(1)

