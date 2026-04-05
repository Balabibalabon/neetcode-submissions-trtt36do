class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        table = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            table[course].append(pre)
        
        def dfs(num_course):
            if num_course in visited:
                return False
            if table[num_course] == []:
                return True
            
            visited.add(num_course)
            for pre in table[num_course]:
                if not dfs(pre):
                    return False
            table[num_course]=[]
            visited.remove(num_course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        