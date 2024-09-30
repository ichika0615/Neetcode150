class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # key: tuple of what alphabets occure and how many times 
                                 # val: list of strings that satisfy their keys.

        for s in strs:
            count = [0] * 26  # a ... z # count := [0, 0, ..., 0]

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()





