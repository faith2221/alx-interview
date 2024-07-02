#!/usr/bin/python3
"""
A Prime game Module.
"""


def isWinner(x, nums):
    """
    Function to find a winner between two players.
    """
    # return none when an invalid option is picked.
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # initializes a list to determine prime status of numbers up to max_num
    is_prime = [True for _ in range(max(max_num + 1, 2))]

    # implement the Sieve of Eratosthenes
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue

        # mark multiples of i as non-prime
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    # mark 0 and 1 as non-prime explicitly
    is_prime[0] = is_prime[1] = False

    # y will count the number of primes up to each index
    y = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            y += 1

        # store the count of primes up to index i in is_prime[i]
        is_prime[i] = y

    player_1 = 0
    for p in nums:
        # Maria wins if the count of primes up to p is odd
        player_1 += is_prime[p] % 2 == 1

    # determine the overall winner
    if player_1 * 2 == len(nums):

        # if Maria and Ben win the same number of rounds, it's a tie
        return None

    if player_1 * 2 > len(nums):

        # Maria wins more rounds than Ben
        return "Maria"

    # Ben wins more rounds than Maria
    return "Ben"
