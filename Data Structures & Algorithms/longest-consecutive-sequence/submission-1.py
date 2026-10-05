class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        seq_len = 1
        for num in nums_set:
            if (num - 1) not in nums_set:
                len_counter = 1
                while (num + 1) in nums_set:
                    len_counter += 1
                    num = num + 1
                if len_counter > seq_len:
                    seq_len = len_counter

        return seq_len