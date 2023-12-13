import heapq

def sliding_subarray_beauty(arr, k, n):
    """
    Find the n-th smallest integer in each contiguous subarray of size k in arr.

    Parameters:
    arr (list): The input array of integers.
    k (int): The size of each subarray.
    n (int): The position of the smallest value in the sorted subarray.

    Returns:
    list: An array containing the n-th smallest integers of each subarray.
    """
    if n > k:
        return []  # n cannot be greater than k

    result = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        heapq.heapify(subarray)
        for _ in range(n):
            nth_smallest = heapq.heappop(subarray)
        result.append(nth_smallest)
    return result

# User input handling
if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the array elements: ").split()))
    k_input = int(input("Enter the subarray length: "))
    n_input = int(input("Enter the position of the smallest value: "))

    result = sliding_subarray_beauty(arr_input, k_input, n_input)
    print(" ".join(map(str, result)))  # Output as a space-separated string


