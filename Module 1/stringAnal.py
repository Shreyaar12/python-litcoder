import sys
def doSomething(email):
    total_chars = len(email)
    uppercase_count = sum(1 for char in email if char.isupper())
    lowercase_count = sum(1 for char in email if char.islower())
    digit_count = sum(1 for char in email if char.isdigit())
    symbol_count = total_chars - (uppercase_count + lowercase_count + digit_count)

    uppercase_percentage = (uppercase_count / total_chars) * 100
    lowercase_percentage = (lowercase_count / total_chars) * 100
    digit_percentage = (digit_count / total_chars) * 100
    symbol_percentage = (symbol_count / total_chars) * 100

    return uppercase_percentage, lowercase_percentage, digit_percentage, symbol_percentage


inputVal = input()    
outputVal = doSomething(inputVal)
for percentage in outputVal:
    print(f"{percentage:.3f}%")
                                          