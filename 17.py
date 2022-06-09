class Link:

  empty = ()

  def __init__(self, first, rest=empty):
    assert rest is Link.empty or isinstance(rest, Link)
    self.first = first
    self.rest = rest

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

