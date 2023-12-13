def people_aware_of_secret(n, delay, forget):
    dp = [1] + [0] * (n - 1)
    mod = 10**9 + 7
    share = 0

    for i in range(1, n):
        if i >= delay:
            share += dp[i - delay]
        if i >= forget:
            share -= dp[i - forget]
        dp[i] = share % mod

    return sum(dp[-forget:]) % mod

# User input handling
if __name__ == "__main__":
    n_input = int(input("Enter the number of days: "))
    delay_input = int(input("Enter the delay day: "))
    forget_input = int(input("Enter the forgetting day: "))

    result = people_aware_of_secret(n_input, delay_input, forget_input)
    print("Number of people aware of the secret:", result)
