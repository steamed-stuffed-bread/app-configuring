# medium
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]: # right part is normal, deal as usual
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]: # left part if normal, deal as usual
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
