"""
Problem Statement:
Find the difference between sum of the squares and square of the sum for the
first 100 natural numbers
"""

import sys

def main():
  args = sys.argv
  if len(args) != 2:
    print_usage()
    return -1

  try:
    limit = int(args[1])
  except:
    print 'limit must be an integer'
    return -1
  
  if limit < 0:
    print 'limit must be non-negative'
    return -1

  sum_of_squares = sum([x * x for x in xrange(1, limit + 1, 1)])
  limit_sum = sum(range(1, limit + 1, 1))
  square_of_sum = limit_sum * limit_sum

  difference = square_of_sum - sum_of_squares

  print 'The difference between the sum of the squares and the square of ' \
      + 'the sum for the first ' \
      + str(limit) \
      + ' natural numbers is ' \
      + str(difference)

def print_usage():
  print 'Usage: python __file__ limit'

if __name__ == "__main__":
  main()
