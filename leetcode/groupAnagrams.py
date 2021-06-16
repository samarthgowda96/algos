from collections import defaultdict
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        groupedWords= defaultdict(list)
        
        for i in strs:
            groupedWords["".join(sorted(i))].append(i)
            
        for g in groupedWords.values():
            res.append(g)
            
        return res
            