class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isduplicate = False
        noduplicate = set(nums)
        if len(nums) != len(noduplicate):
            isduplicate = True
        return isduplicate