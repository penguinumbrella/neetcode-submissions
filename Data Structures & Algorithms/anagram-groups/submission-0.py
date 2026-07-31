class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []


        for s in strs:
            s_counter = Counter(s)

            unique_strs = [sublist[0] for sublist in anagrams]

            is_same = True
            for i, u_s in enumerate(unique_strs):
                if s_counter == Counter(u_s):
                    anagrams[i].append(s)
                    is_same = False
                    break
            
            if is_same: anagrams.append([s])
        
        return anagrams
        



        