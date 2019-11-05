def sort(array: list) -> list:
  # Determine if we need to split the list.
  if len(array) > 1:
    # Split list to to half, @param left, and @param right.
    left = array[:len(array) >> 1]
    right = array[len(array) >> 1:]
    # Sort each list recursively.
    left = sort(left)
    right = sort(right)
    # Re-initialize the array to store result.
    array = list()
    # When there are elements in both @param left, and @param right
    # Pop the smaller element of the 1st element of @param left and @param right, and append it to @param array.
    while len(left) > 0 and len(right) > 0:
      array.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    # If there are remaining elements in @param left or @param right, concatenate them with @param array.
    if left:
      array += left
    elif right:
      array += right
  return array


if __name__ == '__main__':
  print(sort([5, 4, 3, 2, 1]))
