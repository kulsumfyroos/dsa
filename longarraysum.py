def longest_subarray_with_sum_k(arr, k):
    prefix_sum = 0
    sum_indices = {}
    max_length = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        # If the subarray from the start to the current index sums to k
        if prefix_sum == k:
            max_length = i + 1

        # If (prefix_sum - k) is found, calculate the length of the subarray
        if (prefix_sum - k) in sum_indices:
            max_length = max(max_length, i - sum_indices[prefix_sum - k])

        # Only store the first occurrence of each prefix_sum
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i

    return max_length

# Example usage
arr = [1, 2, 3, 7, 5]
k = 12
result = longest_subarray_with_sum_k(arr, k)
print("Length of the longest subarray with sum {}: {}".format(k, result))
