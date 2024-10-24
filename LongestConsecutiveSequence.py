class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = nums.sort()
        length = 0
        longest = 0
        numset = set(nums)

        for n in numset:
            if n-1 in numset:
                continue
            else:
                length = 0
                while n + length in numset:
                    length += 1
            if length > longest:
                longest = length
        return longest
                            

test1 = Solution()
print(test1.longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6])) #Expected output: 7
print(test1.longestConsecutive(nums = [100,4,200,1,3,2])) #Expected output: 4
print(test1.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) #Expected output: 9