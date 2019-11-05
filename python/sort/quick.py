from random import randint


def partition(array, start, end):
  # Partition using Lomuto's partition Scheme.
  index = start - 1
  for i in range(start, end):
    if array[i] < array[end]:
      index += 1
      array[i], array[index] = array[index], array[i]
  array[index + 1], array[end] = array[end], array[index + 1]
  return index + 1


def quick_sort(array, start, end):
  if start < end:
    pivot = randint(start, end)
    array[end], array[pivot] = array[pivot], array[end]
    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)
  return array


def sort(array):
  return quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
  print(sort([5, 4, 3, 2, 1]))
