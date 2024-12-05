def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: Array of size 0 or 1 is already sorted
    pivot = arr[0]  # Choose the first element as the pivot
    left = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to the pivot
    right = [x for x in arr[1:] if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)  # Combine results

# Example usage
arr = list(map(int, input("Enter array elements (space-separated): ").split()))
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
