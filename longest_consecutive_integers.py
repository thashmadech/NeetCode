class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        print(nums_set)
        
        result = 0
        for num in nums_set:
            count = 1
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    count += 1
                    num += 1
                result = max(count, result)
        return result
                    
                    
            
              
            
        
