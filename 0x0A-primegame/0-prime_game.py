#!/usr/bin/python3

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins < ben_wins:
        return "Ben"
    else:
        return "Maria"
