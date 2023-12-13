def longest_common_child(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    # Using two 1D lists to store lengths of longest common suffixes
    dp = [0] * (len_s2 + 1)
    prev_dp = [0] * (len_s2 + 1)

    for i in range(1, len_s1 + 1):
        dp, prev_dp = prev_dp, dp  # Swap references
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev_dp[j - 1] + 1
            else:
                dp[j] = max(prev_dp[j], dp[j - 1])

    return dp[len_s2]

if __name__ == "__main__":
    s1_input = input("Enter the first string: ")
    s2_input = input("Enter the second string: ")

    result = longest_common_child(s1_input, s2_input)
    print("Length of the longest common child string:", result)
