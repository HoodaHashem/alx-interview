#!/usr/bin/python3
"""
minimum operation problem
"""
# def isPrime(n):
#     """isprime function"""
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# def minOperations(n):
#     """solution"""

#     count = 0
#     x = 1
#     past = 0
#     if n == 1 or n == 0:
#         return count
#     if isPrime(n):
#         return n

#     while x < n:
#         if n % x == 0:
#             x *= 2
#             past = x
#             count += 2

#         if n % x != 0:
#             x += past
#             count += 1
#     return count

# print(minOperations(1))    # Expected output: 0 (Base case)
# print(minOperations(2))    # Expected output: 2 (Prime number)
# print(minOperations(3))    # Expected output: 3 (Prime number)
# print(minOperations(4))    # Expected output: 4 (Even number)
# print(minOperations(5))    # Expected output: 5 (Prime number)
# print(minOperations(6))    # Expected output: 5 (Even number with prime factors)
# print(minOperations(7))    # Expected output: 7 (Prime number)
# print(minOperations(8))    # Expected output: 6 (Even number)
# print(minOperations(9))    # Expected output: 6 (Odd number)
# print(minOperations(10))   # Expected output: 7 (Even number)
# print(minOperations(11))   # Expected output: 11 (Prime number)
# print(minOperations(12))   # Expected output: 7 (Even number with non-prime factors)
# print(minOperations(13))   # Expected output: 13 (Prime number)
# print(minOperations(14))   # Expected output: 9 (Even number with multiple factors)
# print(minOperations(15))   # Expected output: 8 (Odd number with multiple factors)
# print(minOperations(16))   # Expected output: 8 (Even number)
# print(minOperations(17))   # Expected output: 17 (Prime number)
# print(minOperations(18))   # Expected output: 8 (Even number with multiple factors)
# print(minOperations(19))   # Expected output: 19 (Prime number)
# print(minOperations(20))   # Expected output: 9 (Even number with multiple factors)
# print(minOperations(21))   # Expected output: 9 (Odd number with multiple factors)
# print(minOperations(22))   # Expected output: 11 (Even number with prime factors)
# print(minOperations(23))   # Expected output: 23 (Prime number)
# print(minOperations(24))   # Expected output: 10 (Even number with multiple factors)
# print(minOperations(25))   # Expected output: 10 (Odd number with prime factors)

from sys import maxsize

def Goal(G, V, J, S):
    if V > G:
        return maxsize
    if V == G:
        return S

    return min(Goal(G, V+J, J, S+1), Goal(G, V*2, V, S+2))

def minOperations(n):
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == maxsize:
        return 0
