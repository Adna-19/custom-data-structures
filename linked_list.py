class Node:
	def __init__(self, data):
		self.data = data
		self.previous = None
		self.next = None

class LinkedList:
	def __init__(self, data):
		self.head = Node(data)

	def add(self, data):
		previous_head = self.head
		self.head = Node(data)
		previous_head.previous = self.head
		self.head.next = previous_head

	def items(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

if __name__ == "__main__":
	linklist = LinkedList(14)
	linklist.add(19)
	linklist.add(38)
	linklist.items()
