class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n =[]
        k = 0
        for num in nums:
            if num == val:
                continue
            n.append(num)
        for i in range(len(n)):
            nums[i] =n[i]
        return len(n)       