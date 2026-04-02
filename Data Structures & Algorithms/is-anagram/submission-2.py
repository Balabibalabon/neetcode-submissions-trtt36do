class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Record = dict()
        for i in s:
            if i not in Record:
                Record[i]=1
            else:
                Record[i]+=1

        # for key in Record.keys():
        #     print(key," ")
        #     print(Record[key])

        for j in t:
            if j not in Record.keys():
                return False
            elif Record[j]==0:
                return False
            else:
                Record[j]-=1
        
        for key in Record.keys():
            if Record[key]>0:
                return False
        return True