class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i + 1, len(nums)):
                if (nums[j] == diff):
                    answer.append(i)
                    answer.append(j)
                    return answer
            diff = target