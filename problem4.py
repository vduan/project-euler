"""
Problem Statement:
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

def is_palindrome(num):
  num_string = str(num)
  string_length = len(num_string)
  for i in xrange((string_length + 1) / 2):
    if num_string[i] != num_string[string_length - i - 1]:
      return False
  return True

def find_palindromes():
  palindromes = []
  for a in xrange(100, 1000):
    for b in xrange(100, 1000):
      product = a * b
      if is_palindrome(product):
        palindromes.append([product, a, b])

  return palindromes

def main():
  args = sys.argv
  if len(args) != 1:
    print_usage()
    return -1

  palindromes = find_palindromes()
  largest_palindrome_data = max(palindromes, key = lambda x:x[0])

  print 'The largest palindrome made from the product of two 3-digit numbers is ' \
    + str(largest_palindrome_data[0]) \
    + ' = ' \
    + str(largest_palindrome_data[1]) \
    + ' x ' \
    + str(largest_palindrome_data[2]) \

def print_usage():
  print 'Usage: python __file__'

if __name__ == "__main__":
  main()
