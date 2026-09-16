class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for i in nums:
            count = 0
            if i-1 not in nums:
                count +=1
                while i+1 in nums:
                    i += 1
                    count +=1
            max_count = max(count, max_count)
        return max_count