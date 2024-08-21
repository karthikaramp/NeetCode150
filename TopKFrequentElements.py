class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        result = []
        while(k):
            max1 = max(hashmap, key=hashmap.get)
            result.append(max1)
            hashmap.pop(max1)
            k = k-1
        return result


test1 = Solution()
test1.topKFrequent(nums = [1, 1, 2, 2, 3], k = 2)
test2 = Solution()
test2.topKFrequent(nums = [1], k = 1)