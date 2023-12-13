def largest_palindrome_optimized(changes, number):
    """
    Function to create the largest palindrome by changing at most 'changes' digits.

    Parameters:
    changes (int): Maximum number of changes allowed.
    number (str): String representation of the integer to be modified.

    Returns:
    str: The largest possible palindrome.
    """
    n = len(number)
    number = list(number)
    changed = [False] * n

    # First pass: Make the number a palindrome
    for i in range(n // 2):
        if number[i] != number[n - 1 - i]:
            if changes > 0:
                max_digit = '9' if changed[i] or changed[n - 1 - i] else max(number[i], number[n - 1 - i])
                number[i] = number[n - 1 - i] = max_digit
                changes -= 1
                changed[i] = changed[n - 1 - i] = True
            else:
                return -1  # Not enough changes to make it a palindrome

    # Second pass: Maximize the palindrome
    i = 0
    while changes > 0 and i < n // 2:
        if number[i] != '9':
            if changed[i] or changed[n - 1 - i]:
                # If already changed, need only one more change to make '9'
                number[i] = number[n - 1 - i] = '9'
                changes -= 1
            elif changes >= 2:
                number[i] = number[n - 1 - i] = '9'
                changes -= 2
        i += 1

    # If there's an odd middle digit, maximize it if possible
    if n % 2 != 0 and changes > 0:
        number[n // 2] = '9'

    return ''.join(number)

# Adding user input handling
if __name__ == "__main__":
    # User inputs the number of changes allowed
    changes_input = int(input())
    
    # User inputs the number as a string
    number_input = input()

    # Running the function and displaying the result
    result = largest_palindrome_optimized(changes_input, number_input)
    print("Largest palindrome:", result)

