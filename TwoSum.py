class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return []


test1 = Solution()
test1.twoSum([2,7,11,15], 9)
test2 = Solution()
test2.twoSum([3,2,4], 6)
test3 = Solution()
test2.twoSum([3,3], 6)