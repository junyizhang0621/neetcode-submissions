
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        store = {}

        for cur_str in strs:
            strArr = [0] * 26
            for s in cur_str:
                strArr[ord(s) - ord('a')] += 1
            
            if str(strArr) not in store:
                store[str(strArr)] = []
                store[str(strArr)].append(cur_str)
            else:
                store[str(strArr)].append(cur_str)
            
        
        res = []
        for key in store:
            res.append(store[key])
        
        return res
