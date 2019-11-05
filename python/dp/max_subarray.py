def max_subarray(array: list) -> list:
  best_sum = current_sum = current_start = best_start = best_end = 0
  for current_end, x in enumerate(array):
    if current_sum <= 0:
      current_start = current_end
      current_sum = x
    else:
      current_sum += x
      if current_sum > best_sum:
        best_sum = current_sum
        best_start = current_start
        best_end = current_end + 1
  return array[best_start:best_end]


if __name__ == '__main__':
  print(max_subarray([5, 4, 3, 2, 1]))
