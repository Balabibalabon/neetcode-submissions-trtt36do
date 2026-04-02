class Solution:
    def isPalindrome(self, s: str) -> bool:

        frontPointer = 0
        if len(s) == 0:
            return False
        endPointer = len(s)-1

        legal_range = []
        Lowercase = range(ord("a"), ord("z")+1) 
        Uppercase = range(ord("A"), ord("Z")+1)
        Alphabetcase = list(Uppercase) + list(Lowercase)
        Alphabetcase_set= set(Alphabetcase)
        Numbercase = range(ord("0"), ord("9")+1)

        legal_range+= Numbercase
        legal_range+= Uppercase
        legal_range+= Lowercase
        legal_set= set(legal_range)

        if len(s) == 0 or len(s) == 1:
            return True
        else:
            while frontPointer < endPointer:
                # frontPointer 要確定是不是在 legal 裡面
                while frontPointer < endPointer and ord(s[frontPointer]) not in legal_set:
                    frontPointer+=1

                # endPointer 要確定是不是在 legal 裡面
                while frontPointer < endPointer and ord(s[endPointer]) not in legal_set:
                    endPointer-=1
                
                print("front:",s[frontPointer],"end:",s[endPointer])
                
                # 確認是否對稱，不對稱就 false
                if s[frontPointer] != s[endPointer]:
                    #確認是否是大小寫問題
                    if (ord(s[frontPointer]) not in Alphabetcase_set) or (ord(s[endPointer]) not in Alphabetcase_set) or abs(ord(s[frontPointer])-ord(s[endPointer]))!=32:
                        return False

                #偶數 return True
                if frontPointer+1 == endPointer:
                    return True

                frontPointer+=1
                endPointer-=1
                
        
        return True #奇數 return True
