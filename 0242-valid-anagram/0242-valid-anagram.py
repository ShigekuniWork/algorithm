from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cal spped O(n)
        # space O(n)
        if len(s) != len(t):
            return False
        
        hash_map = defaultdict(int)
        for c in s:
            hash_map[c] += 1
        
        for c in t:
            if c not in hash_map or hash_map[c] < 1:
                return False
            hash_map[c] -= 1
        
        return True

