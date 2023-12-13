def kth_smallest_trimmed_number(nums, queries):
    answer = []

    for ki, trimi in queries:
        # Trim the numbers to the rightmost 'trimi' digits and store them with their original index
        trimmed_nums = [(num[-trimi:], idx) for idx, num in enumerate(nums)]

        # Sort the trimmed numbers. In case of a tie, the number with the lower index comes first
        trimmed_nums.sort()

        # Append the original index of the kth smallest trimmed number to the answer
        answer.append(trimmed_nums[ki - 1][1])

    return answer

# User input handling
if __name__ == "__main__":
    nums_input = input("Enter the numbers, separated by space: ").split()
    query_count = int(input("Enter the number of queries: "))

    queries = []
    for _ in range(query_count):
        queries.append(list(map(int, input().split())))

    result = kth_smallest_trimmed_number(nums_input, queries)
    print("Result:", ' '.join(map(str, result)))
