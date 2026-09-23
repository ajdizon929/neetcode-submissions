class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        result = []
        buckets = [[] for _ in range(len(nums)+1)]
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        for num in num_freq:
            buckets[num_freq[num]].append(num)

        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        