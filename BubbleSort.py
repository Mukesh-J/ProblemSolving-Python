def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Sorted list: {bubble_sort(unsorted_list)}")