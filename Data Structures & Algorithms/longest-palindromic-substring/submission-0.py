class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)

        table = [[False]*n for _ in range(n)]
        maxLength = 1
        maxstr = s[0]

        # 長度 1
        for i in range(n):
            table[i][i] = True

        # 長度 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                maxLength = 2
                maxstr = s[i:i+2]

        # 長度 >= 3
        for k in range(2, n):
            for j in range(n-k):
                if s[j] == s[j+k] and table[j+1][j+k-1]:
                    table[j][j+k] = True
                    if k+1 > maxLength:
                        maxLength = k+1
                        maxstr = s[j:j+k+1]

        return maxstr