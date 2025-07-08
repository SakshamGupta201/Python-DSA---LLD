def reverseArray(arr, m):
    # Write your code here.
    if m > len(arr) - 1:
        return

    i, j = m + 1, len(arr) - 1

    while i < j:

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def sortedArray(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    res = set()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.add(a[i])
            i += 1
        else:
            res.add(b[j])
            j += 1

    for k in range(i, len(a)):
        res.add(a[k])
    for k in range(j, len(b)):
        res.add(b[k])

    return sorted(res)


def pushZerosAtEnd(arr):
    # write your code here
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr


def findArraySum(a, n, b, m):
    t1 = 0
    t2 = 0

    for el in a:
        t1 = (t1 * 10) + el

    for el in b:
        t2 = (t2 * 10) + el

    sum_str = str(t1 + t2)

    return [int(ch) for ch in sum_str]


def reverseString(s: str) -> str:
    # Write your code from here.
    res = ""
    for el in s.split(" ")[::-1]:
        if el != "" or el != " ":
            res += el
            res += " "
    return res.strip()


def pairSum(arr, s):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                if arr[i] < arr[j]:
                    res.append((arr[i], arr[j]))
                else:
                    res.append((arr[j], arr[i]))

    res.sort()
    return res


from collections import Counter


def highestOccuringChar(string):
    count = Counter(string)
    res_val = -1
    res_ch = ""

    for el, val in count.items():
        if val > res_val:
            res_val = val
            res_ch = el

    return res_ch


def replaceSpaces(s: str):
    # Write your code here.
    return s.replace(" ", "@40")


def removeOccurrences(s: str, part: str) -> str:

    while part in s:
        s = s.replace(part, "", 1)
    return s


s = "aabababa"
part = "aba"

print(removeOccurrences(s, part))
