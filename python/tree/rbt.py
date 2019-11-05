from enum import Enum
from python.tree import Node


class Colour(Enum):
  Red = 1
  Black = 0


class Node(Node):
  def __init__(self, key=None, colour=Colour.Black, parent=None, left=None, right=None):
    super(Node, self).__init__(key, parent, left, right)
    self.colour = colour


class Tree(object):
  def __init__(self):
    self.root = None

  @staticmethod
  def _create_node(key, parent=None, colour=Colour.Red):
    node = Node(key, parent=parent, colour=colour)
    node.left = Node(parent=node)
    node.right = Node(parent=node)
    return node

  @staticmethod
  def _rotate_left(node: Node):
    if node.parent:
      if node.parent.left == node:
        node.parent.left = node.right
      else:
        node.parent.right = node.right
    node.right.parent = node.parent
    node.parent = node.right
    node.right = node.parent.left
    node.right.parent = node
    node.parent.left = node

  @staticmethod
  def _rotate_right(node: Node):
    if node.parent:
      if node.parent.right == node:
        node.parent.right = node.left
      else:
        node.parent.left = node.left
    node.left.parent = node.parent
    node.parent = node.left
    node.left = node.parent.right
    node.left.parent = node
    node.parent.right = node

  def _insert_fixup(self, node):
    while node != self.root and node.parent.colour.value:
      left = node.parent == node.parent.parent.left
      uncle = node.parent.parent.right if left else node.parent.parent.left
      # Case 1 and 4
      if uncle.colour.value:
        node.parent.parent.colour = Colour.Red
        node.parent.colour = Colour.Black
        uncle.colour = Colour.Black
        node = node.parent.parent
      else:
        # Case 2 and 5
        if node == node.parent.right if left else node.parent.left:
          node = node.parent
          if left:
            if node == self.root:
              self.root = node.right
            self._rotate_left(node)
          else:
            if node == self.root:
              self.root = node.left
            self._rotate_right(node)
        node.parent.colour = Colour.Black
        node.parent.parent.colour = Colour.Red
        # Case 3 and 6
        if node.parent.parent == self.root:
          self.root = node.parent
        self._rotate_right(node.parent.parent) if left else self._rotate_left(node.parent.parent)
    self.root.colour = Colour.Black

  def insert(self, key):
    if self.root:
      node = self._create_node(key)
      self._insert(self.root, node)
      self._insert_fixup(node)
    else:
      self.root = self._create_node(key, colour=Colour.Black)

  def _insert(self, parent, node):
    if parent.key > node.key:
      if parent.left.key:
        self._insert(parent.left, node)
      else:
        parent.left = node
        node.parent = parent
    elif parent.key < node.key:
      if parent.right.key:
        self._insert(parent.right, node)
      else:
        parent.right = node
        node.parent = parent
    else:
      raise Exception("Element already exists")

  def _remove_fixup(self, node):
    while (not node.key or not node.colour.value) and node != self.root:
      left = node.parent.left == node
      brother = node.parent.right if left else node.parent.left
      # Case 1
      if brother.colour.value:
        brother.colour = Colour.Black
        node.parent.colour = Colour.Red
        if left:
          self._rotate_left(node.parent)
          brother = node.parent.right
        else:
          self._rotate_right(node.parent)
          brother = node.parent.left
      # Case 2
      if (not brother.left or not brother.left.colour.value) and (not brother.right or not brother.right.colour.value):
        brother.colour = Colour.Red
        node = node.parent
        parent = node.parent
      else:
        # Case 3
        if left:
          if not brother.right or not brother.right.colour.value:
            brother.left.colour = Colour.Black
            brother.colour = Colour.Red
            self._rotate_right(brother)
            brother = node.parent.right
        else:
          if not brother.left or not brother.left.colour.value:
            brother.right.colour = Colour.Black
            brother.colour = Colour.Red
            self._rotate_left(brother)
            brother = node.parent.left
        # Case 4
        brother.colour = node.parent.colour
        node.parent.colour = Colour.Black
        if left:
          brother.right.colour = Colour.Black
          self._rotate_left(parent)
        else:
          brother.left.colour = Colour.Black
          self._rotate_right(parent)
        node = self.root
        break
    if not node:
      node.colour = Colour.Black

  def remove(self, key):
    self._remove(self.root, key)

  def _remove(self, node, key, left=False):
    if node.key:
      if node.key > key:
        self._remove(node.left, key, True)
      elif node.key < key:
        self._remove(node.right, key, False)
      else:
        if not node.left.key:
          if not node.right.key:
            if left:
              node.parent.left = node.right if node.right else None
            else:
              node.parent.right = node.right if node.right else None
        elif not node.right.key:
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
      if not node.colour.value:
        self._remove_fixup(node)
    else:
      raise Exception('Element not found')

  @staticmethod
  def minimum(node):
    while node.left and node.left.key:
      node = node.left
    return node


if __name__ == '__main__':
  tree = Tree()
  tree.insert(5)
  tree.insert(2)
  tree.insert(3)
  tree.insert(8)
  tree.insert(6)
  tree.remove(3)
  print(0)
