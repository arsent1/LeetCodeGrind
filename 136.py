class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                if nums[i] not in nums[1:]:
                    return nums[i]
            else:
                leftlist = nums[:i]
                rightlist = nums[i+1:]
                if (nums[i] not in leftlist) and (nums[i] not in rightlist):
                    return nums[i]