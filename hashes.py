class HashTable:
	def __init__(self):
		self.list = [None] * 11

	@staticmethod
	def hash(n):
		return n % 11

	def set(self, n, v):
		self.list[self.hash(n)] = v

	def get(self, n):
		return self.list[self.hash(n)]

if __name__ == "__main__":
	hash_table = HashTable()
	hash_table.set(1, "Adil")
	hash_table.set(10, "Namra")
	print(hash_table.get(1), hash_table.get(10))
