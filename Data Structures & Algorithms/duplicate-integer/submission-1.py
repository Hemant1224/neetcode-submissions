class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set(nums)
        for i in unique_elements:
            if nums.count(i)>1:
                return True
        else:
            return False

         