import unittest

def ZeroMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    zr = []
    zc = []
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                zr.append(r)
                zc.append(c)
    for x in zr:
        matrix[x] = [0] * columns
    for y in zc:
        for x in range(rows):
            matrix[x][y] = 0
    return matrix
        


class Test(unittest.TestCase):
    data = [([[0,2,3,4],[2,3,4,5],[3,4,5,6]],[[0,0,0,0],[0,3,4,5],[0,4,5,6]]),([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])]

    def test_zero(self):
        for before,after in self.data:
            self.assertEqual(ZeroMatrix(before),after)
    
if __name__ == '__main__':
  unittest.main()