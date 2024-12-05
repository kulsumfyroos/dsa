# Input array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))

# Check if the array is non-empty
if len(arr) == 0:
    print("Array is empty.")
else:
    # Perform left rotation
    first_element = arr.pop(0)  # Remove the first element
    arr.append(first_element)  # Add it to the end of the array

    # Print the rotated array
    print("Array after left rotation by one:", arr)
