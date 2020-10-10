from Stack import Stack
from Queue import Queue
from LinkedList import LinkedList

# Using recursive definition of tree
class BinaryTree:
	
	def __init__(self, root, left=None, right=None):
		self.root = root
		self.left = left
		self.right = right

	# Takes O(n) time to compute the size of tree each time
	def __len__(self):
		total_size = 1
		# adding size of left tree if it exists
		if self.left:
			total_size += len(self.left)
		# adding size of right tree if it exists
		if self.right:
			total_size += len(self.right)
		return total_size

	def get_root(self):
		return self.root

	def set_root(self, new_root):
		self.root = root

	def get_left(self):
		return self.left

	def set_left(self, new_left):
		self.left = new_left

	def get_right(self):
		return self.right

	def set_right(self, new_right):
		self.right = new_right

	def is_leaf(self):
		return (not self.left) and (not self.right)

	# Depth First Search self, and return results as LinkedList
	def dfs(self) -> LinkedList:
		search_result = LinkedList()
		
		dfs_stack = Stack()
		dfs_stack.push(self)
		while dfs_stack:
			cursor = dfs_stack.pop()
			search_result.append(cursor.root)
			if cursor.right:
				dfs_stack.push(cursor.right)
			if cursor.left:
				dfs_stack.push(cursor.left)
		return search_result
	
	# Breadth First Search self, and return results as LinkedList
	def bfs(self) -> LinkedList:
		search_result = LinkedList()

		bfs_queue = Queue()
		bfs_queue.enqueue(self)
		while bfs_queue:
			cursor = bfs_queue.dequeue()
			search_result.append(cursor.root)
			if cursor.left:
				bfs_queue.enqueue(cursor.left)
			if cursor.right:
				bfs_queue.enqueue(cursor.right)
		return search_result
			

if __name__ == '__main__':
	# Building Left tree
	four = BinaryTree(4)
	two = BinaryTree(2, right=four)
	# Building Right tree
	six = BinaryTree(6)
	seven = BinaryTree(7)
	five = BinaryTree(5, left=six, right=seven)
	three = BinaryTree(3, right=five)
	# myTree
	myTree = BinaryTree(1, left=two, right=three)
	print(myTree.dfs())	# Head-> 1-> 2-> 4-> 3-> 5-> 6-> 7
	print(myTree.bfs())	# Head-> 1-> 2-> 3-> 4-> 5-> 6-> 7
