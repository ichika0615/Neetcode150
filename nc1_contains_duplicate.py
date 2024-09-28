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
