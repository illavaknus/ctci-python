import unittest
from collections import Counter

def is_permutation(a, b):
    if len(a) != len(b):
        return False
    cntr = Counter()
    for char in a:
        cntr[char] += 1
    for char in b:
        if cntr[char] == 0:
            return False
        cntr[char] -= 1
    return True
    
    

class TestPermutation(unittest.TestCase):
    false_data = [('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),]
    true_data = [('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),]

    def test_permuation(self):
        for (a,b) in self.true_data:
            # actual = is_unique(data)
            self.assertTrue(is_permutation(a,b))
        for (a,b) in self.false_data:
            # actual = is_unique(data)
            self.assertFalse(is_permutation(a,b))
    
if __name__ == '__main__':
  unittest.main()