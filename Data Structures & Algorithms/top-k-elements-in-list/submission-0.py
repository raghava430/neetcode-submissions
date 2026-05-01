class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # buckets[i] stores numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        # Start from highest frequency
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result