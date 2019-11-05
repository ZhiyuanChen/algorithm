def heapify(array: list, length: int, i: int):
  # Initialize largest as root
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2
  largest = left if left < length and array[largest] < array[left] else largest
  largest = right if right < length and array[largest] < array[right] else largest
  # Change root if needed.
  if largest != i:
    # Perform swap.
    array[i], array[largest] = array[largest], array[i]
    # Heapify the root.
    heapify(array, length, largest)


def sort(array):
  length = len(array)

  # Build a maxheap.
  for i in range(length, -1, -1):
    heapify(array, length, i)
  # Extract elements.
  for i in range(length - 1, 0, -1):
    # Perform swap.
    array[i], array[0] = array[0], array[i]
    heapify(array, i, 0)
  return array


if __name__ == '__main__':
  print(sort([5, 4, 3, 2, 1]))
