class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter

        num = Counter(nums)
        for item, count in num.items():
            if count > 1:
                return True
        return False

        