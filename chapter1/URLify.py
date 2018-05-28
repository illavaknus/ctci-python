import unittest

def URLify(string,length):
    url_index = len(string)
    i = length-1
    # print(string, len(string), length)
    while url_index >= 0:
        # print(string[i],url_index)
        if string[i] == ' ':
            string[url_index-3:url_index] = '%20'
            url_index -= 3
        else:
            string[url_index-1] = string[i]
            url_index -= 1
        i -= 1
    return ''.join(string)

class TestURLify(unittest.TestCase):
    data = [(list('Mr John Smith    '), 13,'Mr%20John%20Smith')]

    def test_urlify(self):
        for (string,length,url) in self.data:
            self.assertEqual(url,URLify(string,length))

if __name__ == '__main__':
    unittest.main()
