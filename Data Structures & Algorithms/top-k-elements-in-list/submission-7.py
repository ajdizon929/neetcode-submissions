class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        sorted_nums = sorted(num_freq, key=num_freq.get)
        return sorted_nums[-k:]
        