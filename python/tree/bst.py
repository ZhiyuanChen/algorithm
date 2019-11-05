from python.tree import *


class Tree(object):
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root:
      self._insert(self.root, Node(key))
    else:
      self.root = Node(key)

  def _insert(self, parent, node):
    if parent.key > node.key:
      if parent.left:
        self._insert(parent.left, node)
      else:
        parent.left = node
        node.parent = parent
    elif parent.key < node.key:
      if parent.right:
        self._insert(parent.right, node)
      else:
        parent.right = node
        node.parent = parent
    else:
      raise Exception("Element already exists")

  def remove(self, key):
    self._remove(self.root, key)

  def _remove(self, node, key, left=False):
    if node:
      if node.key > key:
        self._remove(node.left, key, True)
      elif node.key < key:
        self._remove(node.right, key, False)
      else:
        if not node.left:
          if not node.right:
            if left:
              node.parent.left = node.right if node.right else None
            else:
              node.parent.right = node.right if node.right else None
        elif not node.right:
          if left:
            node.parent.left = node.left
          else:
            node.parent.right = node.left
        else:
          right_minimum = self.minimum(node.right)
          if node.key == self.root.key:
            self.root.key = right_minimum.key
          elif left:
            node.parent.left.key = right_minimum.key
          else:
            node.parent.right.key = right_minimum.key
          self._remove(node.right, right_minimum.key)
    else:
      raise Exception('Element not found')

  @staticmethod
  def minimum(node):
    while node.left:
      node = node.left
    return node


if __name__ == '__main__':
  tree = Tree()
  tree.insert(5)
  tree.insert(2)
  tree.insert(3)
  tree.insert(8)
  tree.insert(6)
  tree.remove(5)
