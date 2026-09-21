class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = set()
        for num in nums:
            if num in checked_nums:
                return True
            else:
                checked_nums.add(num)
        return False