def maximum_subsequence_count(text, pattern):
    """
    Function to determine the maximum number of times the pattern can occur as a subsequence in the modified text.

    Parameters:
    text (str): The original text.
    pattern (str): The pattern string.

    Returns:
    int: The maximum number of times the pattern can occur as a subsequence in the modified text.
    """
    count_first, count_second, total = 0, 0, 0
    for char in text:
        if char == pattern[1]:
            total += count_first
            count_second += 1
        if char == pattern[0]:
            count_first += 1

    return total + max(count_first, count_second)

# User input handling
if __name__ == "__main__":
    text_input = input("Enter the text: ")
    pattern_input = input("Enter the pattern: ")

    result = maximum_subsequence_count(text_input, pattern_input)
    print("Maximum subsequence count:", result)
