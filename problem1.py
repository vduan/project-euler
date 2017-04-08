"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys
import sets

def find_sum(limit):
  threes = set(range(0, limit, 3))
  fives = set(range(0, limit, 5))
  values = threes | fives
  return sum(values)

def main():
  args = sys.argv
  if len(args) != 2:
    print_usage()
    return -1

  try:
    limit = int(args[1])
  except:
    print_usage
    return -1

  if limit < 0:
    print 'limit must be greater than 0'
    return -1

  result = find_sum(limit)

  print 'Sum of all multiples of 3 or 5 below ' + str(limit) + ' is: ' + str(result)

def print_usage():
  print 'Usage: python __file__ limit'

if __name__ == "__main__":
  main()
