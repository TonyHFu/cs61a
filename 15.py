def combo(a, b):
  """
  >>> combo(531, 432)
  45312
  >>> combo(531, 4321)
  45321
  >>> combo(1234, 9123)
  91234
  >>> combo(0, 321)
  321

  """
  if a == 0 or b == 0:
    return a + b
  elif a % 10 != b % 10:
    a_combo = combo(a // 10, b) * 10 + a % 10
    b_combo = combo(a, b // 10) * 10 + b % 10
    return min(a_combo, b_combo)
  return combo(a // 10, b //10) * 10 + a % 10 
