# Trees


# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


ex1 = tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])])

def count_nodes(t):
    """
    >>> count_nodes(ex1)
    9
    """
    if is_leaf(t):
        return 1

    total = 0
    for b in branches(t):
        total += count_nodes(b)

    return total + 1

def count_nodes_alt(t):
    """
    >>> count_nodes_alt(ex1)
    9
    """
    return sum([count_nodes_alt(b) for b in branches(t)], 1)


ex2 = tree('D', [tree('B', [tree('A'), tree('C')]), tree('F', [tree('E'), tree('H', [tree('G'), tree('I')])])])

def collect_leaves(t):
    """
    >>> collect_leaves(ex2)
    ['A', 'C', 'E', 'G', 'I']
    """
    if is_leaf(t):
      return [label(t)]
    
    # leaves = []
    # for b in branches(t):
    #   leaves += collect_leaves(b)
    # return leaves
    
    return sum ([collect_leaves(b) for b in branches(t)], [])

def fib(n):
  if n == 1 or n == 2:
    return 1
  return fib(n - 1) + fib(n - 2)

def fib_tree(n):
    """
    >>> print_tree(fib_tree(4))
    3
     1
      0
      1
     2
      1
      1
       0
       1
    """
    if n <= 1:
      return tree(n)
    prev = fib_tree(n - 1)
    prev2 = fib_tree(n - 2)
    return tree(label(prev) + label(prev2), [prev2, prev])

def print_tree(t, indent=0):
  """
  >>> print_tree(fib_tree(4))
  3
   1
    0
    1
   2
    1
    1
     0
     1
  """
  
  print(" " * indent + str(label(t)))
  for b in branches(t):
    print_tree(b, indent + 1)

def print_calls(name, f):
    def new_f(t):
        print('Name:', name)
        print('Inputted Tree:')
        print_tree(t)
        input()
        ret = f(t)
        print('Returned:', ret)
        return ret
    return new_f

# collect_leaves = print_calls('collect_leaves', collect_leaves)

def tiny_print(t):
    print('tree(', label(t), sep='', end='')
    
    if not is_leaf(t):
        print(', [', sep='', end='')
        for b in branches(t):
            tiny_print(b)
        print(']', sep='', end='')
    print(')', sep='', end='')



def square_tree(t):
  """
  >>> tiny_print(square_tree(tree(2)))
  tree(4)
  """
  # if is_leaf(t):
  #   return tree(label(t) ** 2)
  
  return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])


