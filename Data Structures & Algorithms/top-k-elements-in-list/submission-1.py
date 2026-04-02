class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        R_dict = dict()
        for number in nums:
            if number not in R_dict.keys():
                R_dict[number] = 1
            else:
                R_dict[number] += 1
        
        key_list = list(R_dict.keys())
        value_list = list(R_dict.values())

        m_dict = defaultdict(list)
        for i in range(len(key_list)):
            m_dict[value_list[i]].append(key_list[i])
        count_list = list(m_dict.keys())
        sorted_list = sorted(count_list,reverse=True)

        count = 0
        Result = []
        for j in sorted_list:
            reduandent = k-count
            if reduandent > k:
                Result += m_dict[j][:reduandent]
                count += reduandent
            
            else:
                Result += m_dict[j]
                count += len(m_dict[j])

            if count>=k:
                return Result


