class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key:num  val:occurence
        
        freq = [[] for _ in range(len(nums) + 1)] # idx:occurence val: list of nums that occure certain times
        
        #count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #freq
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
