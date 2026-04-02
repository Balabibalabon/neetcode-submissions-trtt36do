class Solution:
    
    def encode(self, strs: List[str]) -> str:
        l_length = len(strs)
        length_str = "" + str(l_length) + "^"
        msg_str = ""
        for context in strs:
            msg_str += context
            w_length = len(context)
            length_str += str(w_length) + "|"
        print(length_str + msg_str)
        return length_str + msg_str

    def decode(self, s: str) -> List[str]:
        word_length = []
        count = 0
        tmp = ""
        flag = False
        front_Pointer = 0
        for i in s:
            front_Pointer += 1
            if flag:
                if i != "|":
                    tmp += i
                else:
                    word_length.append(int(tmp))
                    count+=1
                    tmp = ""
                if count == word_num:
                    break
            elif i != "^":
                tmp += i
            else:
                word_num = int(tmp)
                tmp = ""
                flag = True

        Result = []
        for length in word_length:
            # if length == 0:
            #     return [""]
            # else:
            end_Pointer = front_Pointer + int(length)
            word = s[front_Pointer:end_Pointer]
            Result.append(word)
            front_Pointer = end_Pointer
        return Result
