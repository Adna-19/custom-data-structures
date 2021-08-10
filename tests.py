import unittest
from my_array import DynamicArray, StaticArray

class DynamicArrayTests(unittest.TestCase):
	""" Test cases for Dynamic Array DS """
	@classmethod
	def setUp(cls):
		cls.data = DynamicArray([1, 2, 3, 4, 5], int)

	def test_add_item(self):
		for item in ('5', True, 3.2):
			self.assertRaises(TypeError, self.data.add_item, item)
		self.assertEqual(self.data.add_item(6), [1, 2, 3, 4, 5, 6])

	def test_insert_item(self):
		self.assertEqual(self.data.insert_item(0, 0), [0, 1, 2, 3, 4, 5])
		self.assertRaises(IndexError, self.data.insert_item, 6, 7)
		self.assertRaises(TypeError, self.data.insert_item, '7')

	def test_remove_functions(self):
		self.data = DynamicArray([1, 2, 4, 3, 4, 4, 4], int)
		self.assertEqual(self.data.remove_item(4), [1, 2, 3, 4, 4, 4])
		self.assertEqual(self.data.remove_last_item(4), [1, 2, 3, 4, 4])
		self.assertEqual(self.data.remove_specific_item_at(2), [1, 2, 4, 4])

class StaticArrayTests(unittest.TestCase):
	""" Test cases for Static Array DS """
	@classmethod
	def setUp(cls):
		cls.data = StaticArray([1, 2, 3, 4, 5], int, 6)

	def test_add_item(self):
		self.assertEqual(self.data.add_item(6), [1, 2, 3, 4, 5, 6])
		self.assertRaises(IndexError, self.data.add_item, 7)

	def test_insert_item(self):
		self.assertEqual(self.data.insert_item(6, 5), [1, 2, 3, 4, 5, 6])
		self.assertRaises(IndexError, self.data.insert_item, 7, 6)

if __name__ == "__main__":
	unittest.main()
