class TimeMap:

    def __init__(self):
        self.diction = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(key, value, timestamp)
        save = self.diction.get(key, [[],[]])
        print(save)
        save[0].append(timestamp)
        print(save[0])
        save[1].append(value)
        print(save[1])
        print(save)
        self.diction[key] = save
    def get(self, key: str, timestamp: int) -> str:
        container = self.diction.get(key, None)
        if not container:
            return ""
        print(container)
        index = container[0]
        l, r = 0, len(index)-1
        res = -1
        while l<=r:
            m = (l+r)//2
            if index[m]<=timestamp:
                res = max(res, m)
                l = m+1
            else:
                r = m-1
        if res == -1:
            return ""
        return container[1][res]
            

