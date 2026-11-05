class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                popped_i = stack.pop()
                diff = i - popped_i
                result[popped_i] = diff
            stack.append(i)
        return result