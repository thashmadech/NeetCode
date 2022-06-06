class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for i in nums:
            if i in seen_set:
                return True
            seen_set.add(i)
            
            
