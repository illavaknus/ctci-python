import unittest # learn more: https://python.org/pypi/unittest

def is_unique(string):
  s = set()
  for c in string:
    if c in s:
      return False
    s.add(c)
  return True

class Test(unittest.TestCase):
  trueData = [('python'),('abcdefghijklmnopqrstuvwxyz1234567890')]
  falseData = [('yellow submarine'),('novacaine')]

  def test_unique(self):
    for data in self.trueData:
      # actual = is_unique(data)
      self.assertTrue(is_unique(data))
    for data in self.falseData:
      # actual = is_unique(data)
      self.assertFalse(is_unique(data))
    
if __name__ == '__main__':
  unittest.main()