def isPresent(arr: list[list[int]], target: int) -> bool:
    for el_arr in arr:
        for el in el_arr:
            if el == target:
                return True

    return False


def row_wise_sum(arr: list[list[int]]) -> int:
    for el_arr in arr:
        curr_sum = 0
        for el in el_arr:
            curr_sum += el
        print("Sum is", curr_sum)


def col_wise_sum(arr: list[list[int]], row, col):
    for i in range(col):
        sum = 0
        for j in range(row):
            sum += arr[j][i]
        print(sum)


def largest_row_sum(arr) -> int:
    max_sum, max_sum_row = float("-inf"), float("-inf")
    for i, el_arr in enumerate(arr):
        curr_sum = 0
        for el in el_arr:
            curr_sum += el
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_row = i
    return max_sum_row


def wavePrint(arr, nRows, mCols):
    res = []
    for i in range(mCols):
        if i % 2 == 0:
            res.extend(top_to_bottom(arr, nRows, i))
        else:
            res.extend(bottom_to_top(arr, nRows, i))
    return res


def top_to_bottom(arr, row, col):
    res = []
    for j in range(row):
        res.append(arr[j][col])
    return res


def bottom_to_top(arr, row, col):
    res = []
    for j in range(row - 1, -1, -1):
        res.append(arr[j][col])
    return res


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    startingRow, startingCol = 0, 0
    endingRow, endingCol = rows - 1, cols - 1

    while startingRow <= endingRow and startingCol <= endingCol:

        for i in range(startingCol, endingCol + 1):
            res.append(matrix[startingRow][i])
        startingRow += 1

        for i in range(startingRow, endingRow + 1):
            res.append(matrix[i][endingCol])
        endingCol -= 1

        if startingRow <= endingRow:
            for i in range(endingCol, startingCol - 1, -1):
                res.append(matrix[endingRow][i])
            endingRow -= 1

        if startingCol <= endingCol:
            for i in range(endingRow, startingRow - 1, -1):
                res.append(matrix[i][startingCol])
            startingCol += 1

    return res


def rotateMatrix(matrix):
    transposeMatrix(matrix)

    matrix.reverse()
    return matrix


def transposeMatrix(matrix: list[list[int]]):

    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def findInMatrix(x, arr):
    row = len(arr)
    col = len(arr[0])

    start = 0
    end = (row * col) - 1

    while start <= end:
        mid = start + (end - start) // 2

        el = arr[mid // col][mid % col]
        if el == x:
            return True
        elif el < x:
            start = mid + 1
        else:
            end = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(findInMatrix(13, matrix))
