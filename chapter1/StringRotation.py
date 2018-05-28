import unittest

def is_substring(string, sub):
    return string.find(sub) != -1

def is_rotation(base,rotation):
    if len(base) == len(rotation):
        return is_substring(base+base,rotation)
    return False

class Test(unittest.TestCase):
    trueData = [('waterbottle', 'erbottlewat')]
    falseData = [('foo', 'bar'),('foo', 'foofoo')]

    def test_rotation(self):
        for (string,rotation) in self.trueData:
            self.assertTrue(is_rotation(string,rotation))
        for (string,rotation) in self.falseData:
            self.assertFalse(is_rotation(string,rotation))
    
if __name__ == '__main__':
  unittest.main()
