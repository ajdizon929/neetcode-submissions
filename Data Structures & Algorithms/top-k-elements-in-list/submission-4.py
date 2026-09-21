class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        k_count = 0

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
            if (k_count >= k):
                break
            if bucket:
                for num in bucket:
                    result.append(num)
                    k_count += 1
        
        return result

        
