def sort(array: list) -> list:
  # @param i indicates the position of the current element being sorted.
  # We assume the first element is already sorted.
  # Hence, we start from the first element instead of zeroth.
  for i in range(1, len(array)):
    # @param key stores the value of current element.
    key = array[i]
    # @param j indicates the element to the left of the current element.
    j = i - 1
    # Compare if the current element is less than jth element.
    # If so, move the jth element to j+1th position.
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j -= 1
    # When there is no element greater than the current element.
    # Insert the current element to this position.
    # Notice that the current element is greater than any other element to its left.
    array[j + 1] = key
  return array


if __name__ == '__main__':
  print(sort([5, 4, 3, 2, 1]))
