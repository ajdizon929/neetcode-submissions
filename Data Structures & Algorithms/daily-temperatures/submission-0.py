class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures[1:], start=1):
            if temp <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    popped_i = stack.pop()
                    diff = i - popped_i
                    result[popped_i] = diff
                stack.append(i)
        return result