# Input array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))

# Assume the array is sorted initially
is_sorted = True

# Check if the array is sorted
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:  # If any element is greater than the next
        is_sorted = False
        break

# Print the result
if is_sorted:
    print("The array is sorted.")
else:
    print("The array is not sorted.")
