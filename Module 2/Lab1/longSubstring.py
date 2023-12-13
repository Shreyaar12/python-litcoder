def length_of_longest_substring(s):
    """
    Function to find the length of the longest substring without repeating characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repeating characters.
    """
    char_index = {}
    max_length = start = 0

    for i, char in enumerate(s):
        # If character is found in the dictionary and it's index is on or after the start of the current substring
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Update the start to the index after the repeating character
        char_index[char] = i  # Update the last index of the character
        max_length = max(max_length, i - start + 1)

    return max_length

# User input handling
if __name__ == "__main__":
    string_input = input("Enter the string: ")
    result = length_of_longest_substring(string_input)
    print("Length of the longest substring:", result)

