class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap for input (number, index)
        index_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_dict:
                return [index_dict[difference], i]
            index_dict[nums[i]] = i
            