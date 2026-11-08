class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        max_left = height[0]
        max_right = height[-1]
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                total_water += (max_left - height[l])
                l += 1
            else:
                max_right = max(max_right, height[r])
                total_water += (max_right - height[r])
                r -= 1

        return total_water