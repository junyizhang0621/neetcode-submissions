class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        all_hash = {}

        for word in strs:
            cur_hash = [0] * 26
            for l in word:
                cur_hash[ord(l)-97] += 1
            cur_hash = str(cur_hash)
            #print(cur_hash)
            if cur_hash not in all_hash:
                all_hash[cur_hash] = [word]
            else:
                all_hash[cur_hash].append(word)
        
        output = []

        for i in all_hash:
            output.append(all_hash[i])
        return output
            

        