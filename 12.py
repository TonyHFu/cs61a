mem = []
def fib_mem(n):
  """
  >>> fib_mem(5)
  5
  """
  if n <= 1:
    return n
  if n > len(mem):
    mem.extend([-1 for _ in range(n + 1 - len(mem))])
  if mem[n] == -1:
    new_mem = fib_mem(n - 1) + fib_mem(n - 2)
    mem[n] = new_mem
  return mem[n]
  
def exp(b, n):
  if n == 0:
    return 1
  i = 1
  curr = b
  while i < n:
    if n >= i * 2:
      curr *= curr
      i *= 2
    else:
      curr *= b
      i += 1
  return curr
  

