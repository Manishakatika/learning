class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Sort_s = sorted(s)
        Sort_t = sorted(t) 
        return sorted(s) == sorted(t)
        
