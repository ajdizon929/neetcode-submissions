class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        maxl_array = [0]*len(height)
        maxr_array = [0]*len(height)
        # Calculate max heights, skipping first/last index respectively
        for i in range(1, len(height)):
            maxl_array[i] = max(maxl_array[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            maxr_array[i] = max(maxr_array[i+1], height[i+1])
        
        # skip first/last index
        for i in range(1, len(height)-1):
            # look at max height to the left and right of the index
            max_l = maxl_array[i]
            max_r = maxr_array[i]
            # calculate how much water is trapped
            trapped_water = min(max_l,max_r) - height[i]
            # handle negative values
            total_water += max(0,trapped_water)
        return total_water