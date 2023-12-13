def clumsy_factorial(n):
    """
    Calculate the clumsy factorial of a positive integer n.

    Parameters:
    n (int): A positive integer.

    Returns:
    int: The clumsy factorial of n.
    """
    if n <= 0:
        return 0

    # Stack to store the intermediate results
    stack = [n]
    n -= 1
    operation_index = 0  # 0: multiply, 1: divide, 2: add, 3: subtract

    while n > 0:
        if operation_index == 0:  # Multiplication
            stack.append(stack.pop() * n)
        elif operation_index == 1:  # Division
            stack.append(stack.pop() // n)
        elif operation_index == 2:  # Addition
            stack.append(n)
        else:  # Subtraction
            stack.append(-n)

        n -= 1
        operation_index = (operation_index + 1) % 4

    # Sum up the values in the stack for the final result
    return sum(stack)

# User input handling
if __name__ == "__main__":
    n_input = int(input("Enter a positive integer: "))
    result = clumsy_factorial(n_input)
    print("Clumsy factorial:", result)
