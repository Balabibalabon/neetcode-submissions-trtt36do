class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_list = []
        for i in range(len(position)):
            car_list.append((position[i],speed[i]))
        car_sort = sorted(car_list, key = lambda car_p: car_p[0], reverse=True)
        print(car_sort)

        for car in car_sort:
            if not stack:
                stack.append(car)
            else:
                prev_car = stack[-1]
                new_car = car
                t_prev = (target-prev_car[0]) / prev_car[1]
                print(f"前面這台需要 {t_prev} 到達終點")
                t_new = (target-new_car[0]) / new_car[1]
                print(f"後面這台需要 {t_new} 到達終點")
                if t_new <= t_prev:
                    # 表示會追上
                    pass
                else:
                    stack.append(new_car)
        return len(stack)