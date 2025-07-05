from collections import defaultdict


def swap_alternate(arr: list[int]) -> None:
    i = 0

    while i + 1 < len(arr):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 2


def find_unique(arr):
    unique = 0

    for el in arr:
        unique ^= el
    return unique


def unique_no_of_occurances(arr: list[int]) -> bool:

    d = defaultdict(int)

    for el in arr:
        d[el] += 1

    s = set()

    for key, value in d.items():
        if value in s:
            return False
        s.add(value)

    return True


def find_dups(arr: list[int]) -> int:

    ans = 0

    for el in arr:
        ans ^= el

    for i in range(1, len(arr)):
        ans ^= i

    return ans


def all_dups(nums: list[int]) -> list[int]:
    res = []

    # for i in range(len(arr)):
    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            res.append(abs(num))
        else:
            nums[index] = -nums[index]
    return res


def intersection_of_two_sorted_arrays(A: list[int], B: list[int]) -> list[int]:
    i = j = 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return res


def pairSum(arr: list[int], S: int) -> list[list[int]]:
    res = []
    seen = []

    for el in arr:
        num = S - el
        if num in seen:
            count = 0
            while num in seen:
                seen.remove(num)
                count += 1
                if num < el:
                    res.append([num, el])
                else:
                    res.append([el, num])
            while count:
                seen.append(num)
                count -= 1
        seen.append(el)

    return sorted(res)


def sort_01(arr: list[int]) -> None:
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] == 1:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1


def binary_search(arr: list[int], key: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


class Solution:
    def find_first(self, arr: list[int], key: int) -> int:
        start = 0
        end = len(arr) - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == key:
                res = mid
                end = mid - 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return res

    def find_last(self, arr: list[int], key: int) -> int:
        start = 0
        end = len(arr) - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == key:
                res = mid
                start = mid + 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return res

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.find_first(nums, target), self.find_last(nums, target)]

    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        start, end = 0, len(arr) - 1

        while start <= end:

            mid = (start + end) // 2

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                end = mid - 1
            else:
                start = mid + 1

    def pivot_element(self, arr: list[int]) -> int:

        start, end = 0, len(arr) - 1

        while start < end:

            mid = (start + end) // 2

            if arr[mid] < arr[0]:
                end = mid
            else:
                start = mid + 1

        return start

    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        pivot = self.pivot_element(nums)

        # Decide which part to search: [pivot, end] or [start, pivot-1]
        if nums[pivot] <= target <= nums[-1]:
            start = pivot
            end = len(nums) - 1
        else:
            start = 0
            end = pivot - 1

        # Standard binary search
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def findPages(self, arr: list[int], n: int, m: int) -> int:
        start = 0
        end = sum(arr)
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if self.isPossibleSol(arr, mid, m):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def isPossibleSol(self, arr: list[int], sol: int, m: int) -> bool:
        student_count = 1
        curr_sum = 0

        for pages in arr:
            if pages > sol:
                return False  # Single book exceeds current mid, not possible

            if curr_sum + pages <= sol:
                curr_sum += pages
            else:
                student_count += 1
                curr_sum = pages
                if student_count > m:
                    return False

        return True


n = 4
m = 2
arr = [10, 20, 30, 40]
sol = Solution()
print(sol.findPages(arr, n, m))
