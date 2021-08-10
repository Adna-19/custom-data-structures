def type_is_valid(data_items, type_class):
	""" Helper function to check type of each item """
	for item in data_items:
		if type(item) != type_class:
			raise TypeError("Array must have all same type elements")
	return True

class DynamicArray:
	""" A dynamic array DS holds undefined no of items """
	def __init__(self, data_items, type_class):
		if type_is_valid(data_items, type_class):
			self.data_items = data_items
			self.type_class = type_class

	def add_item(self, item):
		""" Appends item to the array after type validation """
		if type(item) == self.type_class:
			self.data_items.append(item)
		else:
			raise TypeError("Item type not matched with defined type")
		return self.data_items

	def insert_item(self, item, index):
		""" Inserts item at a specific index """
		if len(self.data_items) == 0 or len(self.data_items) == index:
			self.data_items.append(item)
		elif index > len(self.data_items):
			raise IndexError("No such index exists")
		else:
			# make an empty memory location for adjustment
			self.data_items.append(None)
			for i in range(len(self.data_items)-2, index-1, -1):
				self.data_items[i+1] = self.data_items[i]

			if type(item) == self.type_class:
				self.data_items[index] = item
			else: raise TypeError("Item type not matched with defined type")
		return self.data_items

	def remove_item(self, item):
		""" Remove 1st occurrence of item """
		if item not in self.data_items:
			raise ValueError("No such item founded.")
		del self.data_items[self.data_items.index(item)]
		return self.data_items

	def remove_last_item(self, item):
		""" Remove last occurrence of an item """
		if item not in self.data_items:
			raise ValueError("No such item founded.")
		self.data_items = self.data_items[::-1]
		del self.data_items[self.data_items.index(item)]
		self.data_items = self.data_items[::-1]
		return self.data_items

	def remove_specific_item_at(self, index):
		""" Remove specific element on a specific position"""
		if not self.data_items[index]:
			raise ValueError("No such item founded.")
		del self.data_items[index]
		return self.data_items

	def display(self):
		""" Displays all items to the console """
		return [item for item in self.data_items]


class StaticArray(DynamicArray):
	""" A static array DS holds defined no of items """
	def __init__(self, data_items, type_class, no_of_items):
		super().__init__(data_items, type_class)
		self.no_of_items = no_of_items

	def add_item(self, item):
		if len(self.data_items) == self.no_of_items:
			raise IndexError("Items exceeding from defined limit")
		super(StaticArray, self).add_item(item)
		return self.data_items

	def insert_item(self, item, index):
		if len(self.data_items) == self.no_of_items:
			raise IndexError("Items exceeding from defined limit")
		super(StaticArray, self).insert_item(item, index)
		return self.data_items


if __name__ == "__main__":
	numbers = StaticArray([1, 2, 3, 4], int, 10)

	# print(numbers.display())
	numbers.add_item(5)
	numbers.add_item(6)
	numbers.add_item(7)
	# numbers.remove_specific_item_at(2)
	print(numbers.display())
