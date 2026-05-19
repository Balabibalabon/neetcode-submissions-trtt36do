class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target = [0]*26
        search = [0]*26
        for i in s1:
            target[ord(i)-ord('a')] += 1
        for i in range(len(s2)-len(s1)+1):
            for j in range(i,i+len(s1)):
                search[ord(s2[j])-ord('a')]+=1
            if search == target:
                return True
            search = [0]*26
        return False