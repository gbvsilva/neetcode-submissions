class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key=lambda x: -x[0])
        print(cars)
        for position, speed in cars:
            time = (target - position) / speed
            if stack and stack[-1] >= time:
                pass
            else:
                stack.append(time)
        return len(stack) 