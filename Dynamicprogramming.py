def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of LIS:", longest_increasing_subsequence(arr))

