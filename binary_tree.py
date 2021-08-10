class Node:
	"""Binary tree node"""
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

class BinaryTree:
	"""This class represents a binary tree data structure"""
	def __init__(self, root):
		""" :param root: Binary tree node """
		self.root = root

if __name__ == "__main__":
	tree = BinaryTree("a")
	tree.left = Node("b")
	tree.right = Node("c")
	tree.left.left = Node("d")
	tree.right.right = Node("e")
