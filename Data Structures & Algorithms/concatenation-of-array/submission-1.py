class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # import copy
        # n = len(nums)
        # ans = copy.deepcopy(nums)
        # # print(ans)
        # for i in range(n):
        #     ans.append(nums[i])
        # print(ans)
        ans = nums + nums
        return ans


        