def recursive_insertion_sort(arr, n):
    # Base case: If size is 1, it's already sorted
    if n <= 1:
        return

    # Recursively sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element into the correct position in the sorted part
    key = arr[n - 1]
    j = n - 2

    # Shift elements greater than key to the right
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Place the key in its correct position
    arr[j + 1] = key


# Input array from the user
n = int(input("Enter the size: "))
arr = []
print("Enter array elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Call the recursive insertion sort function
recursive_insertion_sort(arr, n)

# Print the sorted array
print("Sorted array:", arr)
