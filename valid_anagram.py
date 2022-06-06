class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_s = "".join(sorted_s)
        sorted_t = sorted(t)
        sorted_t = "".join(sorted_t)
        if sorted_s == sorted_t:
            return True
        
        
        
