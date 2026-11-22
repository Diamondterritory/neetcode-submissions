class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product, right_product = [1], [1]
        n = len(nums)
        for i in range(1,len(nums)+1):
            left_product.append(left_product[i-1]*nums[i-1])
            right_product.append(right_product[i-1]*nums[n-i])

        ans = []
        for j in range(len(nums)):
            ans.append(left_product[j]*right_product[n-j-1])

        return ans