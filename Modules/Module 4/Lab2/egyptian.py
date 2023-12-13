def egyptian_fraction(numerator, denominator):
    unit_fractions = []

    while numerator != 0:
        # Find the smallest unit fraction that can be subtracted from the fraction
        unit_denominator = (denominator + numerator - 1) // numerator
        unit_fractions.append(unit_denominator)

        # Update the fraction
        numerator = numerator * unit_denominator - denominator
        denominator *= unit_denominator

    return unit_fractions

# User input handling
if __name__ == "__main__":
    numerator_input = int(input("Enter the numerator: "))
    denominator_input = int(input("Enter the denominator: "))

    result = egyptian_fraction(numerator_input, denominator_input)
    print("Egyptian fraction representation:")
    for denom in result:
        print(denom)
