class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #  using a sorting technique
        nums.sort()
        return nums[len(nums) // 2]



        