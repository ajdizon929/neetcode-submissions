class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numMap.keys():
                if numMap[difference] != i:
                    return [i, numMap[difference]]
            