class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_e = {}
        for key, val in enumerate(nums):
            if target-val not in dict_e.keys():
                dict_e.update({val: key})
            else:
                index_1 = key
                index_2 = dict_e[target-val]
        return index_1, index_2
        
        
        
        
                


       
            
                
        
