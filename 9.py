from array import array


def isPal(x):
  """
  >>> isPal([1,2,1])
  True
  >>> isPal([2,3,4])
  False
  """
  assert type(x) == list, "isPal expects a list object"
  for i in range(len(x) // 2):
    if x[i] != x[-i - 1]:
      return False
  return True

def isPalN(n, lst):
  """
  >>> isPalN(2, [1,2,1])
  Is not a palindrome
  >>> isPalN(3, [1,2,1,2])
  Is a palindrome
  """
  assert type(lst) == list, "isPalN expects lst to be a list object"
  assert type(n) == int, "isPalN expects n to be an integer"
  assert n <= len(lst), "isPalN expects n to be less or equal to the length of lst"

  if isPal(lst[:n]):
    print("Is a palindrome")
  else:
    print("Is not a palindrome")