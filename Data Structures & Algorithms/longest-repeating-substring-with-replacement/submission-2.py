class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l ,r = 0, 0
        record = {}
        res = 0
        while r < len(s):
            record[s[r]] = 1 + record.get(s[r], 0) #掃到的 char 加入 dict
            print("加入 ", s[r], "目前 dict 裡面有:", record.keys(), "各有:", record.values()," 個")

            while ((r-l+1) - self.get_max_in_dict(record)) > k :
                record[s[l]] = record.get(s[l], 0) - 1 #移除左邊 char record
                l += 1
            
            res = max(res, r-l+1)
            r += 1
            
            print(res)
                
        return res
    
    def get_max_in_dict(self, record: dict) -> int:
        return max(record.values())

