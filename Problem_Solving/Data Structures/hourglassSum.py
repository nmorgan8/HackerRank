def hourglassSum(arr):
    result_list = []
    for row in range(1, len(arr) - 1):
        for col in range(1, len(arr[0]) - 1):
            result_list.append(arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1] +
                               arr[row][col] + arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1])
    return max(result_list)
