class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0

        if nums[-1] < target :
            return len(nums)
            
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i - 1] < target and nums[i] > target:
                return i
        