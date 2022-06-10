from pickle import FALSE


class Tree:
  def __init__(self, label, branches=[]):
    for b in branches:
      assert isinstance(b, Tree)
    self.label = label
    self.branches = branches
  
  def is_leaf(self):
    return not self.branches
  
  def __repr__(self):
    if self.branches == []:
      return 'Tree(' + str(self.label) + ')'
    else:
      return 'Tree(' + str(self.label) + ', [' + ', '.join(str(b) for b in self.branches) + '])'

def print_tree(t, indent=0):
  print(" " * indent, t.label)
  for b in t.branches:
    print_tree(b, indent + 1)

def tree_map(f, t):
  t.label = f(t.label)
  for b in t.branches:
    map(f, b)

def prune(t, x):
  """
  >>> x = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
  >>> prune(x, 1)
  >>> print_tree(x)
   3
    2
  """

  t.branches = [b for b in t.branches if b.label != x]

  for b in t.branches:
    prune(b, x)
  
class Link:

  empty = ()

  def __init__(self, first, rest=empty):
    assert rest is Link.empty or isinstance(rest, Link)
    self.first = first
    self.rest = rest

  def __repr__(self):
    if self.rest is Link.empty:
      return 'Link(' + repr(self.first) + ')'
    else:
      return 'Link(' + repr(self.first) + ', ' + repr(self.rest) + ')'
  
  def __str__(self):
    ans = "<"
    while self.rest is not Link.empty:
      ans += str(self.first) + ", "
      self = self.rest
    return ans + str(self.first) + '>'
  
  def __eq__(self, other):
    # if self is Link.empty or other is Link.empty:
    #   return self is Link.empty and other is Link.empty
    # if type(self.first) == type(other.first):
    #   return self.first == other.first and self.rest == other.rest
    # else:
    #   return False

    if self.first != other.first:
      return False
    return self.rest == other.rest
    
  def __contains__(self, x):
    if self.first == x:
      return True
    return x in self.rest

  def __add__(self, other):
    if self.rest is Link.empty:
      if other.rest is Link.empty:
        return Link(self.first, Link(other.first))
      else:
        return Link(self.first, Link(other.first) + Link(other.rest))
    else:
      return Link(self.first, self.rest + other)
    

  def __mul__(self, num):
    ans = self
    for i in range(num - 1):
      ans += self
    return ans

  def __rmul__(self, num):
    return self * num
    

def sum_link(link):
  if link is Link.empty:
    return 0
  return link.first + sum_link(link.rest)

def display_link(link):
  ans = "< "
  while link is not Link.empty:
    if isinstance(link.first, Link):
      elem = display_link(link.first)
    else:
      elem = str(link.first)
    ans += elem + " "
    link = link.rest
  ans += ">"
  return ans

def map(f, lnk):

  """
  >>> lnk = Link(1, Link(2, Link(3)))
  >>> map(lambda x: x * 2, lnk)
  >>> display_link(lnk)
  '< 2 4 6 >'
  """

  # if lnk is Link.empty:
  #   return Link.empty
  # return Link(f(lnk.first), map(f, lnk.rest))
  
  # curr = lnk
  # first = curr
  # while lnk is not Link.empty:
  #   curr.first = f(lnk.first)
  #   lnk = lnk.rest
  #   curr = curr.rest
  # return first


  # while lnk is not Link.empty:
  #   lnk.first = f(lnk.first)
  #   lnk = lnk.rest

  if lnk is Link.empty:
    return
  lnk.first = f(lnk.first)
  map(f, lnk.rest)