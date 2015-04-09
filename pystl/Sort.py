""" implement basic sorting algorithms. """
import math
import pdb

def insertion_sort(arr, offset = 0, gap = 1):
  for i in range(offset+gap, len(arr), gap):
    # search.
    j = i
    for jj in range(offset, i, gap):
      if arr[jj] > arr[i]:
        j = jj
        break
    if j != i:
      # move
      temp = arr[i]
      for k in range(i, j, -gap):
        arr[k] = arr[k-gap]
      arr[j] = temp
  return arr

def shell_sort(arr):
  n = len(arr)
  for k in range(1, int(math.log(n, 2))+2):
    gap = 2 * int(n / 2**(k+1)) + 1
    for offset in range(gap):
      insertion_sort(arr, offset, gap)
  return arr

if __name__ == '__main__':
  # print insertion_sort([3, 4, 5, 7, 1, 6], 1, 2)
  print shell_sort([3, 4, 5, 7, 1, 6])

