class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsToSet = set(nums)
        if len(nums) != len(numsToSet):
            return True
        return False

test1 = Solution()
test2 = Solution()
test3 = Solution()
print(test1.containsDuplicate([1,2,3,1]))  #As the array contains duplicate, the object return True
print(test2.containsDuplicate([1,2,3,4]))  #As the array doesnot contain duplicate, the object returns False
print(test3.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) #As the array contains duplicate, the object returns True