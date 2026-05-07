class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # minimum is on the right side
                l = mid + 1
            else:
                # minimum is at mid or on the left side
                r = mid

        return nums[l]