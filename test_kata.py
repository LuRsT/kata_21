from unittest import TestCase

from kata import List


class TestList(TestCase):

    def test_index(self):
        le_list = List()
        with self.assertRaises(ValueError):
            le_list.index("fred")

    def test_append(self):
        le_list = List()
        le_list.append("fred")

        self.assertEqual(0, le_list.index("fred"))
        with self.assertRaises(ValueError):
            le_list.index("wilma")

    def test_append_twice(self):
        le_list = List()
        le_list.append("fred")
        le_list.append("wilma")
        self.assertEqual(0,  le_list.index("fred"))
        self.assertEqual(1, le_list.index("wilma"))
        self.assertEqual(["fred", "wilma"], [v for v in le_list])

    def test_delete(self):
        le_list = List()
        le_list.append("fred")
        le_list.append("betty")
        le_list.append("gil")
        le_list.append("ian")
        with self.assertRaises(IndexError):
            le_list.delete(4)
        self.assertEqual(["fred", "betty", "gil", "ian"], [v for v in le_list])
        le_list.delete(2)
        self.assertEqual(["fred", "betty", "ian"], [v for v in le_list])
        le_list.delete(0)
        self.assertEqual(["betty", "ian"], [v for v in le_list])
        le_list.delete(le_list.index("betty"))
        self.assertEqual(["ian"], [v for v in le_list])
        le_list.delete(le_list.index("ian"))
        self.assertEqual([], [v for v in le_list])
        with self.assertRaises(IndexError):
            le_list.delete(0)


