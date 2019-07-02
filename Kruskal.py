class DisjointSet:
  def __init__(self, objects):
    self.numberOfComponents = len(objects)
    self.ids = list(range(len(objects)))
    self.map = { val:i for i, val in enumerate(objects) }
    self.sizes = [1] * len(objects)

  def union(self, obj1, obj2):
    root1 = self.find(obj1)
    root2 = self.find(obj2)

    if root1 == root2:
      return False

    if self.sizes[root1] < self.sizes[root2]:
      self.ids[root1] = root2
      self.sizes[root2] += self.sizes[root1]
      self.sizes[root1] = 0
    else:
      self.ids[root2] = root1
      self.sizes[root1] += self.sizes[root2]
      self.sizes[root2] = 0

    self.numberOfComponents -= 1

    return True


  def find(self, obj):
    obj_id = self.map[obj]
    orig_id = obj_id
    while self.ids[obj_id] != obj_id:
      obj_id = self.ids[obj_id]

    while orig_id != obj_id:
      old_id = self.ids[orig_id]
      self.ids[orig_id] = obj_id
      orig_id = old_id

    return obj_id


class Kruskal:
  def __init__(self, cities):
    self.cities = sorted(cities, key=lambda x: x[-1])
    self.uniqueCities = set()
    for citya, cityb, dist in cities:
      self.uniqueCities.update([citya, cityb])
    self.dset = DisjointSet(self.uniqueCities)
  
  def findMST(self):
    mst = []
    for citya, cityb, dist in self.cities:
      if self.dset.numberOfComponents == 1:
        return mst
      if not self.dset.union(citya, cityb):
        continue
      mst.append([citya, cityb, dist])
    return []

inputs = [
  [["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]],
  [["Acity","Bcity",2], ["Bcity","Dcity",5], ["Acity","Dcity",4], ["Ccity","Ecity",1]]
]

for inp in inputs:
  kruskal = Kruskal(inp)
  print(kruskal.findMST())

