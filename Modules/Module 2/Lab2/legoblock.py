def lego_blocks(n, m):
    MOD = 10**9 + 7

    # Calculate the number of ways to build one row of the wall
    row_combinations = [1, 1, 2, 4]
    while len(row_combinations) <= m:
        row_combinations.append(sum(row_combinations[-4:]) % MOD)

    # Calculate the number of ways to build the entire wall without restrictions
    total = [pow(c, n, MOD) for c in row_combinations]

    # Calculate the number of ways to build the wall with the restriction of no vertical breaks
    # This is done by excluding the 'unstable' configurations
    unstable = [0, 0]
    for i in range(2, m + 1):
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)

    return (total[m] - unstable[m]) % MOD

# User input handling
if __name__ == "__main__":
    n_input = int(input("Enter the height of the wall (n): "))
    m_input = int(input("Enter the width of the wall (m): "))

    result = lego_blocks(n_input, m_input)
    print("Number of ways to build the wall:", result)
