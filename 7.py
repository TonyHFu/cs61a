def cascade(n):
  print(n)
  if n >= 10:
    cascade(n // 10)
    print(n)

# cascade(486)
    
def fib(n):
  assert n >= 0
  if n <= 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

# print(fib(5))

def count_partition(n, m):
  if m == 0 or n < 0:
    return 0
  if n == 0:
    return 1
  return count_partition(n - m, m) + count_partition(n, m - 1)

print(count_partition(6, 4))


  