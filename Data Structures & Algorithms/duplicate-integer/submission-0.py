class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counted_nums = Counter(nums)
        for item in counted_nums.values():
            if item != 1:
                return True
        return False


        