class MyIterator:
  def __init__(self):
    self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.index = 0

  def __iter__(self):
    return iter(self.data)

  def __next__(self):
    if self.index < 5:
      x = self.data[self.index]
      self.index += 1
      return x
    else:
      self.index = 0
      raise StopIteration

  # def __getitem__(self, index):
  #   return self.data[index]

demo = MyIterator()

while True:
  try:
    print(next(demo))
  except StopIteration:
    break

# for i in demo:
#   print(i)