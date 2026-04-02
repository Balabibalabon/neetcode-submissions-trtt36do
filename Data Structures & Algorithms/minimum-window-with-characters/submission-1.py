class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = {}
        for i in t:
            table[i] = 1 + table.get(i, 0)
        print(table)
        cri = 0 # 紀錄符合 table 要求的數量
        cri_list = [] # 紀錄那些 cha 符合 table 要求
        test_tab = {key:0 for key in table.keys()}
        l = 0
        r = 0
        res = str("1"*len(s))
        ever_reach = False
        while r<len(s):
            # 新增進 test_tab
            if s[r] in test_tab.keys():
                test_tab[s[r]] = 1 +  test_tab.get(s[r], 0)
                # 確認原本是否符合要求
                if s[r] in cri_list:
                    pass
                # 確認新增後是否符合要求
                else:
                    if test_tab[s[r]] >= table[s[r]]:
                        cri_list.append(s[r])
                        cri+=1
                    print(s[r],"符合規範")
                print("test_tab 目前狀態為:", test_tab)
            while cri == len(table.keys()) and l<=r:
                if r-l+1 <= len(res):
                    res = s[l:r+1]
                    print("符合規範，更新 res:", res)
                    ever_reach = True
                if s[l] in table.keys():
                    print("左指針往右移動時，", s[l], "被移除")
                    test_tab[s[l]] -= 1
                    print("在剩下的區間裡，", s[l], "剩下", test_tab[s[l]], "個")
                    if test_tab[s[l]] < table[s[l]]:
                        cri_list.remove(s[l])
                        cri -= 1
                l+=1
            r+=1
            print("目前l:",l, "目前r:",r, "res:", res)
        if not ever_reach:
            return ""
        else:
            return res