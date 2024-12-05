# Input array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))

if len(arr) < 2:
    print("Array must have at least two distinct elements.")
else:
    # Initialize variables
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    # Find smallest and second smallest
    for num in arr:
        if num < smallest:
            second_smallest, smallest = smallest, num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    # Find largest and second largest
    for num in arr:
        if num > largest:
            second_largest, largest = largest, num
        elif num > second_largest and num != largest:
            second_largest = num

    # Check for valid second smallest and second largest
    if second_smallest == float('inf') or second_largest == float('-inf'):
        print("Array must have at least two distinct elements.")
    else:
        print("Second Smallest Element:", second_smallest)
        print("Second Largest Element:", second_largest)
