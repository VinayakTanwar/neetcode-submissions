class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs: 
            sorted_s = "".join(sorted(word))
            if sorted_s not in seen: 
                seen[sorted_s] = [word]
            else:
                seen[sorted_s].append(word)

        return list(seen.values())  
    