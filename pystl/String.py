# basic utils for string operations.
import math
import pdb

def robin_karp(text, pattern):
  """implements the basic robin-karp randomized algorithm for string matching 
      input:
        text: the source text for matching patterns.
        pattern: the pattern string.
  """
  alpha = 3
  M = 8191
  m = len(pattern)
  npow = int(math.log(m-1) / math.log(2))
  alphas = range(npow+1)
  alphas[0] = alpha
  for i in range(1, npow+1):
    alphas[i] = (alphas[i-1] ** 2) % M

  def pow(order):
    res = 1
    digit = 0
    while order > 0:
      if order % 2 == 1:
        res = (res * alphas[digit]) % M
      digit += 1
      order = int(order / 2)
    return res

  def hash(text, i):
    assert(i+m <= len(text))
    res = 0
    for j in range(i, i+m):
      res += pow(m-1-(j-i)) * ord(text[j])
      res %= M
    return res

  ph = hash(pattern, 0)
  pt = hash(text, 0)
  for i in range(len(text)-m+1):
    if pt == ph:
      if text[i:i+m] == pattern:
        return i
    elif i < len(text)-m:
      pt = alpha * (pt - pow(m-1) * ord(text[i])) + ord(text[i+m])
      pt %= M
  return -1





