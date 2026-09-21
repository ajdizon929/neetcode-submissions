class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        # Get frequencies
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Make buckets
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        # Put numbers in buckets
        for num in nums:
            if num not in buckets[freq[num]]:
                buckets[freq[num]].append(num)

        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result

        
