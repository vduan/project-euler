"""
Problem Statement:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys

def prime_factorization(num):
  factors = []
  i = 2
  n = num

  while i * i <= n:
    if n % i:
      i += 1
    else:
      n /= i
      factors.append(i)
  if n > 1:
    factors.append(n)

  return factors

def main():
  args = sys.argv
  if len(args) != 2:
    print_usage()
    return -1

  try:
    num  = int(args[1])
  except:
    print_usage
    return -1

  if num < 1:
    print 'num must be greater than 1'
    return -1

  prime_factors = prime_factorization(num)

  max_prime_factor = max(prime_factors)

  print 'The largest prime factor of ' + str(num) + ' is ' + str(max_prime_factor)

def print_usage():
  print 'Usage: python __file__ num'

if __name__ == "__main__":
  main()
