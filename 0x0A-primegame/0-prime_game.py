#!/usr/bin/python3
""" 
the prime game module
"""


def isWinner(x, nums):
    """
    This implementation directly determines the winner based on 
    whether n is even or odd, without the need for simulating the game
    """
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
