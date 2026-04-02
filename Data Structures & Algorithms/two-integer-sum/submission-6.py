class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Record = dict()
        position = 0
        for i in nums:
            if i not in Record.keys():
                Record[i]=[position]
            else:
                Record[i].append(position)
            position+=1
        first_value_list = list(Record.keys())
        for key in Record.keys():
            if target-key in first_value_list:
                if key == target-key:
                    if len(Record[key])>1:
                        return [Record[key][0],Record[key][1]]
                    else:
                        continue
                if Record[key][0]<Record[target-key][0]:
                    return [Record[key][0],Record[target-key][0]]
                else:
                    return [Record[target-key][0],Record[key][0]]
