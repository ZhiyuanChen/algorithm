import unittest
import random
from . import insertion, merge


class SortTest(unittest.TestCase):

  @staticmethod
  def shuffle(array):
    result = array.copy()
    random.shuffle(result)
    return result

  def setUp(self):
    self.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.test_list = [self.shuffle(self.array) for _ in range(100)]

  def testInsertion(self):
    for l in self.test_list:
      assert self.array == insertion.sort(l)

  def testMerge(self):
    for l in self.test_list:
      assert self.array == merge.sort(l)


if __name__ == "__main__":
  unittest.main()
