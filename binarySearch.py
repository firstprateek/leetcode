def binarySearch(target, array, low, high):
  while low <= high:
    mid = (low + high) // 2
    print('low: {}, high: {}, mid: {}'.format(low, high, mid))
    if target == array[mid]: return mid

    if target > array[mid]:
      low = mid + 1
    else:
      high = mid - 1

  return low - 1

print(binarySearch(5.5, [1,2,3,4,5,6,7], 0, 6))