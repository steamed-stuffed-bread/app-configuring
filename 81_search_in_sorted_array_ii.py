# medium
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                return True
            # only when there is duplicate between mid and right, nums[mid] == nums[right], because in normal case,
            # nums[mid] should be either larger than nums[right] when index < mid is normal
            # or smaller than nums[right] when index > mid is normal
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            elif nums[mid] > nums[right]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                right = right - 1
        return False
