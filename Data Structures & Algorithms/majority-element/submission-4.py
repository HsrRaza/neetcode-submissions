class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using a hashmap
        count = defaultdict(int)
        res = maxCount =0

        for num in nums:
            count[num] +=1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res





        

#Algorithm
# Create a hash map to store element frequencies.
# Initialize res and maxCount to track the current best candidate.
# For each element num:
# Increment its count in the hash map.
# If its count exceeds maxCount, update res = num and maxCount = count[num].
# Return res.



        