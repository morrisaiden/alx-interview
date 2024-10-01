#!/usr/bin/python3
"""
prime numbers, game theory, and algorithm optimization
"""


def isWinner(x, nums):
    """
    Determine the winner of the game between Maria and Ben based on the given
    rounds of prime picking and removing multiples.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list where each element is n for each round,
        representing
                     the upper bound of numbers from 1 to n to play the game.

    Returns:
        str: "Maria" if Maria wins the most rounds, "Ben" if Ben wins the most
             rounds, or None if there is a tie.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False
    primes = [i for i in range(2, max_num + 1) if sieve[i]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:

            ben_wins += 1
            continue
        primes_removed = set()
        player_turn = 0

        for prime in primes:
            if prime > n:
                break

            if prime not in primes_removed:

                for multiple in range(prime, n + 1, prime):
                    primes_removed.add(multiple)

                player_turn = 1 - player_turn

        if player_turn == 1:

            maria_wins += 1
        else:

            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
