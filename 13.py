def fib_iter(n):
  """
  >>> x = fib_iter(4)
  >>> next(x)
  0
  >>> next(x)
  1
  >>> next(x)
  1
  >>> next(x)
  2
  """

  # arr = []

  # def fib(n):
  #   if n <= 1:
  #     arr[n] = n
  #   if n > len(arr):
  #     arr.extend([-1 for _ in range(n + 1 - len(arr))])
  #   if arr[n] == -1:
  #     result  = fib(n - 1) + fib(n - 2)
  #     arr[n] = result
  #   return arr[n]
  
  # fib(n)

  curr, prev = 1, 0
  arr = [prev, curr]
  i = 2
  while i < n:
    curr, prev = prev + curr, curr
    arr.append(curr)
    i += 1
  return iter(arr)

# arr = []

# def fib(n):
#   if n <= 1:
#     return n
#   if n > len(arr):
#     arr.extend([-1 for _ in range(n + 1 - len(arr))])
#   if arr[n] == -1:
#     result  = fib(n - 1) + fib(n - 2)
#     arr[n] = result
#   return arr[n]