# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    letters = set([char for char in s])
    ans = []
    for letter in letters:
        ans += [(letter, s.count(letter))]
    return ans

frequencies("aaacbbb")