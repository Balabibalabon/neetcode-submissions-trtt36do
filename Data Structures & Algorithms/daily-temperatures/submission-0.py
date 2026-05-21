class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            index = i
            day = i+1
            temperature = temperatures[index]
            if not stack:
                stack.append([temperature, day])
            while stack and stack[-1][0] < temperature:
                _, h_d = stack.pop()
                res[h_d-1] = day-h_d
            stack.append([temperature, day])
        while stack:
            day = len(temperatures)+1
            _, h_d = stack.pop()
            res[h_d-1] = 0
        return res
        