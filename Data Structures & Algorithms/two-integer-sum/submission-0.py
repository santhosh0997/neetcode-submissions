class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            if target - nums[i] in l:
                return [l.index(target - nums[i]), i]
            else:
                l.append(nums[i])
        