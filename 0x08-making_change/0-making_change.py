#!/usr/bin/python3
"""
 This function initializes a dynamic programming table (dp)
 to store the minimum number of coins needed for each total amount
 from 0 to the target total.
 """


def makeChange(coins, total):
    """
     It iterates through each coin and updates the table accordingly
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:

        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
