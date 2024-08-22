
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1]
        prod = 1
        for i in range (0, len(nums)-1):
            prod *= nums[i]
            answer.append(prod)
        prod = 1
        for j in range (len(nums)-1, 0, -1):
            prod *= nums[j]
            answer[j-1] *= prod
        print(f"answer: {answer}")




test1 = Solution()
test1.productExceptSelf([1,2,3,4])
test2 = Solution()
test2.productExceptSelf([-1,1,0,-3,3])
