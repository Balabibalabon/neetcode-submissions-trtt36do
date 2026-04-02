from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Result = defaultdict(list)

        for context in strs:
            index_list = [0]*26
            for char in context:
                index_list[ord(char)-ord("a")] += 1
            Result[tuple(index_list)].append(context)
        return list(Result.values())
