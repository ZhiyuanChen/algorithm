from random import randint


def partition(array, start, stop):
  # Partition using Lomuto's partition Scheme.
  index = start - 1
  for i in range(start, stop):
    if array[i] < array[stop]:
      index += 1
      array[i], array[index] = array[index], array[i]
  array[index + 1], array[stop] = array[stop], array[index + 1]
  return index + 1


def quick_sort(array, start, stop):
  if start < stop:
    pivot = randint(start, stop)
    array[stop], array[pivot] = array[pivot], array[stop]
    p = partition(array, start, stop)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, stop)
  return array


def sort(array):
  return quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
  print(sort([5, 4, 3, 2, 1]))
