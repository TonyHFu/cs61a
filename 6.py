def count_up(n):
  """
  >>> count_up(1)
  1
  """
  if n == 1:
    print(n)
  else:
    count_up(n-1)
    print

# count_up(10)

def sum_digits(n):
  """
  >>> sum_digits(9)
  9
  >>> sum_digits(19)
  10
  >>> sum_digits(2019)
  12
  """
  if n < 0:
    return n
  else:
    return n % 10 + sum_digits(n // 10)

