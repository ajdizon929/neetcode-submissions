class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        suf = [1]*len(nums)
        res = [1]*len(nums)
        ## assemble the prefix array
        for i in range(len(nums)):
            if (i == 0):
                pre[i] = 1
            else:
                pre[i] = pre[i-1]*nums[i-1]

        ## assemble the suffix array
        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                suf[i] = 1
            else:
                suf[i] = suf[i+1]*nums[i+1]

        for i in range(len(nums)):
            res[i] = pre[i]*suf[i]

        return res