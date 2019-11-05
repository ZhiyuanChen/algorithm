class Node(object):
  def __init__(self, parent=None, key=None, left=None, right=None):
    self.parent = parent
    self.key = key
    self.left = left
    self.right = right


class Tree(object):
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root:
      self._insert(self.root, key)
    else:
      self.root = Node(None, key)

  def _insert(self, node: Node, key, parent=None, left=False):
    if not node:
      if left:
        parent.left = Node(parent, key)
      else:
        parent.right = Node(parent, key)
    else:
      if key < node.key:
        self._insert(node.left, key, node, True)
      elif key > node.key:
        self._insert(node.right, key, node, False)
      else:
        raise Exception("Element already exists")

  def delete(self, key):
    self._delete(self.root, key)

  def _delete(self, node, key, left=False):
    if node:
      if node.key > key:
        self._delete(node.left, key, True)
      elif node.key < key:
        self._delete(node.right, key, False)
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
          self._delete(node.right, right_minimum.key)
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
  tree.delete(5)
