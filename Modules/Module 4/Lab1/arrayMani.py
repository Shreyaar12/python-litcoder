def mix_the_array(n, queries):
    arr = [0] * (n + 1)

    for start, end, value in queries:
        arr[start - 1] += value
        if end < n:
            arr[end] -= value

    max_value, current = 0, 0
    for val in arr:
        current += val
        max_value = max(max_value, current)

    return max_value

# User input handling
if __name__ == "__main__":
    n_input = int(input("Enter the array size: "))
    q_input = int(input("Enter the number of queries: "))

    queries = []
    for _ in range(q_input):
        queries.append(list(map(int, input().split())))

    result = mix_the_array(n_input, queries)
    print("Maximum value in the array:", result)
