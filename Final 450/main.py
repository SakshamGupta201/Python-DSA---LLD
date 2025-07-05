import heapq
from typing import List


class Solution:
    def reverseArray(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]

            low += 1
            high -= 1

    def get_min_max(self, arr):
        if not arr:
            return None, None

        n = len(arr)
        if n == 1:
            return arr[0], arr[0]

        # Initialize min and max based on first two elements
        if arr[0] < arr[1]:
            min_val, max_val = arr[0], arr[1]
        else:
            min_val, max_val = arr[1], arr[0]

        i = 2
        while i < n - 1:
            if arr[i] < arr[i + 1]:
                min_val = min(min_val, arr[i])
                max_val = max(max_val, arr[i + 1])
            else:
                min_val = min(min_val, arr[i + 1])
                max_val = max(max_val, arr[i])
            i += 2

        # If odd number of elements, handle last one
        if n % 2 != 0:
            min_val = min(min_val, arr[-1])
            max_val = max(max_val, arr[-1])

        return min_val, max_val

    def kthSmallest(self, arr, k):
        heapq.heapify(arr)
        for _ in range(k - 1):
            heapq.heappop(arr)
        return arr[0]

    def sort012(self, arr):
        low = mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:

                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:

                mid += 1
            else:

                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

    def findUnion(self, a, b):
        res = set()

        for el in a:
            res.add(el)
        for el in b:
            res.add(el)

        return len(res)

    def rotate(self, arr):
        temp = arr[-1]

        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = temp

    #

    def maxSubArraySum(self, arr):
        max_sum = curr_sum = arr[0]

        for el in arr[1:]:
            curr_sum = max(el, curr_sum + el)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < m:
            res.extend(nums1[i:])
        else:
            res.extend(nums2[j:])

        nums1 = res

nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol = Solution()
print(sol.merge(nums1, m, nums2, n))
