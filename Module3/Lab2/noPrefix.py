def check_passwords(passwords):
    passwords.sort()  # Sort the passwords to bring potential prefixes next to each other
    for i in range(len(passwords) - 1):
        # Check if the current password is a prefix of the next
        if passwords[i] == passwords[i + 1][:len(passwords[i])]:
            return f"BAD PASSWORD"
    return "GOOD PASSWORD"

# User input handling
if __name__ == "__main__":
    passwords_input = input("Enter the passwords, separated by space: ").split()
    result = check_passwords(passwords_input)
    print(result)
