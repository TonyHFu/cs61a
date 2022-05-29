def fact(n):
    if n == 1:
      return 1
    if n < 1:
      return 0
    return n * fact(n - 1)

def expand(expr):
  [base, exp] = expr.split("^")
  exp = int(exp)

  if exp == 0:
    return 1
  if exp == 1:
    return base[1:-1]

  ans = ""

  first_sign = 1
  second_sign = 1
  if base[0] == "-":
    first_sign = -1
    base = base[1:]
  if "-" in base:
    second_sign = -1
  
  [first, second] = base.split(r"[+-]")
  first_coef = int(first.translate(None, r"\d")) * first_sign
  first_term = first.translate(None, r"!\d")
  second_coef = int(second.translate(None, r"\d")) * second_sign
  second_term = second.translate(None, r"!\d")
  
  for k in range(exp):
    coef = fact(exp) / (fact(k) * fact(exp - k))
    first_exp = k
    second_exp = exp - k
    if coef == 0:
      pass
    if first_exp != 0:
      coef *= first_coef
    if second_exp != 0:
      coef *= second_coef
    ans += coef
    if first_exp != 0:
      ans += first_term + "^" + str(first_exp)
    if second_exp != 0:
      ans += second_term + "^" + str(second_exp)

  return ans
    



