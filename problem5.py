"""
Problem Statement:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Notes:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

We can filter out smaller numbers that are represented by their larger multiples.
so, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 can all be removed, leaving us with:
11 12 13 14 15 16 17 18 19 20

Some of these are prime, we'll need any number we have to be divisible by all of them:
2 3 5 7 11 13 17 19
Their product is 9,699,690, so this is a good base

We can also ignore all the numbers <10 because they will be covered by their higher multiples

This leaves us with the remaining numbers:
12 14 15 16 18 20
close enough, let's just test these as divisors and move on

"""

import sys

def find_smallest_multiple():
  base = 9699690

  value = base
  divisors = [12, 14, 15, 16, 18, 20]
  passes = True
  while True:
    for d in divisors:
      if value % d != 0:
        value += base
        passes = False
      if not passes:
        break
    if passes:
      break
    passes = True
  return value

def did_it_work(num):
  'testing num = ' + str(num)
  for d in xrange(1, 21, 1):
    if num % d != 0:
      print 'nope. not divisible by ' + str(d)
      return

  print 'nice, seems to work'


def main():
  args = sys.argv
  if len(args) != 1:
    print_usage()
    return -1

  smallest_multiple = find_smallest_multiple()

  print 'The smallest number that can be divided evenly by all ints from 1 to 20 inclusive is '\
      + str(smallest_multiple)

  print 'testing...'
  did_it_work(smallest_multiple)

def print_usage():
  print 'Usage: python __file__'

if __name__ == "__main__":
  main()
