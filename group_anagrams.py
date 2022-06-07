class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_list = defaultdict(list)
        for i in strs:
            temp_list[str(sorted(i))].append(i)
        res = list(temp_list.values())
        return res
       
        
       
