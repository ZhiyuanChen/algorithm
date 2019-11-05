import unittest
import random
from time import time
from python.sort import insertion, merge, heap, quick, test


class SortTest(unittest.TestCase):

  @staticmethod
  def shuffle(array):
    result = array.copy()
    random.shuffle(result)
    return result

  def setUp(self):
    self.array = [i for i in range(1000)]
    self.test_list = [self.shuffle(self.array) for _ in range(100)]

  def testInsertion(self):
    t = time()
    for l in self.test_list:
      assert self.array == insertion.sort(l)
    print(time() - t)

  def testMerge(self):
    t = time()
    for l in self.test_list:
      assert self.array == merge.sort(l)
    print(time() - t)

  def testHeap(self):
    t = time()
    for l in self.test_list:
      assert self.array == heap.sort(l)
    print(time() - t)

  def testQuick(self):
    t = time()
    for l in self.test_list:
      assert self.array == quick.sort(l)
    print(time() - t)

  def testTest(self):
    for l in self.test_list:
      assert self.array == test.sort(l)


if __name__ == "__main__":
  unittest.main()
