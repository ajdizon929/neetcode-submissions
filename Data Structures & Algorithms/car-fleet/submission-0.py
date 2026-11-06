class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        order = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        for i in order:
            time = (target - position[i]) / speed[i]
            if (not stack) or (time > stack[-1]):
                stack.append(time)
        return len(stack)