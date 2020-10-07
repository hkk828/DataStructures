class Stack:
	'''
	Implementation of Stack using python dictionary.
	Each value gets the key = 0, 1, 2, ... and highest key is on the top of the Stack.
	'''

	def __init__(self):
		self.stack = {}
		self.size = 0

	def __len__(self):
		return self.size

	def __repr__(self):
		repr_str = "Bottom "
		for idx in range(self.size):
			val = self.stack[idx]
			repr_str += str(val) + " "
		repr_str += "Top ->"
		return repr_str

	def push(self, val):
		self.stack[self.size] = val
		self.size += 1

	def peek(self):
		if self.size == 0:
			print("Empty Stack!")
			return
		return self.stack[self.size-1]

	def pop(self):
		if self.size == 0:
			raise Exception("Can't pop from an empty Stack!")
		
		pop_value = self.stack.pop(self.size-1)
		self.size -= 1
		return pop_value

if __name__ == '__main__':
	myStack = Stack()
	myStack.push(1)
	myStack.push(2)
	myStack.push(3)
	print(myStack)	# Bottom 1 2 3 Top ->

	print(myStack.peek())	# 3
	print(len(myStack))	# 3
	
	while myStack:
		print(myStack.pop())	# 3 2 1
	
	print("Below shows the result of pop on empty Stack")
	myStack.pop()	# Error "Can't pop from an empty Stack!"
