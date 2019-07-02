class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LRUcache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = {}
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.cursize = 2

  def get(self, key):
    if key in self.storage:
      node = self.storage[key]
      self._remove(node)
      self._add(node)

      return node.val

    return -1

  def put(self, key, value):
    node = None
    if key in self.storage: self._remove(node)

    node = Node(key, value)
    self.storage[key] = node
    self._add(node)
    if len(self.storage) > self.capacity:
      lru_node = self.head.next
      del self.storage[lru_node.key]
      self._remove(lru_node)

  def _remove(self, node):
    prev = node.prev
    prev.next = node.next
    prev.next.prev = prev

  def _add(self, node):
    prev = self.tail.prev
    prev.next = node
    node.prev = prev
    node.next = self.tail
    self.tail.prev = node
