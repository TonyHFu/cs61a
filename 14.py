from _10 import *

def count_groupings(n):
  if n <= 2:
    return 1
  
  return sum([count_groupings(i) * count_groupings(n - i) for i in range(1, n)])



def replace_with_sum(t):
  if is_leaf(t):
    return tree(label(t))
  new_branches = [replace_with_sum(b) for b in branches(t)]
  branch_sum = sum([label(b) for b in new_branches])
  return tree(label(t) + branch_sum, new_branches)




