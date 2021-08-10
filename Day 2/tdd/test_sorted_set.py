import unittest
from sorted_set import SortedSet


class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([6, 7, 3]))


class TestSizeProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([1])
        self.assertEqual(len(s), 1)

    def test_one(self):
        s = SortedSet([1, 1, 1])
        self.assertEqual(len(s), 1)


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])
        self.assertIsNotNone(s)

    def test_sequence(self):
        s = SortedSet([7, 8])
        self.assertSequenceEqual([7, 8], s.list)

    def test_duplicates(self):
        s = SortedSet([7, 8, 9, 9, 1, 2])
        self.assertSequenceEqual([1, 2, 7, 8, 9], s.list)

    def test_sorted(self):
        s = SortedSet([7, 8, 9, 9, 1, 2])
        self.assertSequenceEqual([1, 2, 7, 8, 9], s.list)

    def test_from_iterable(self):
        g = SortedSet((7, 8, 4, 6, 7))
        self.assertSequenceEqual([4, 6, 7, 8], g.list)


if __name__ == '__main__':
    unittest.main()
