class Queue:
	'''
	Implementation of Queue using python dictionary.
	Initially key is given as key = 0, 1, 2, 3, 4, ... with lowest key is removed first.
	As dequeue() is applied, we decrease the initial index (init_idx) one by one.
	With slight modifications one can also implement 'deque' (double-ended queue).
	'''

	def __init__(self):
		self.queue = {}
		self.init_idx = 0
		self.size = 0

	def __len__(self):
		return self.size

	def __repr__(self):
		repr_str = "<- Front "
		for idx in range(self.size):
			val = self.queue[self.init_idx + idx]
			repr_str += str(val) + " "
		repr_str += "End"
		return repr_str
	

	def enqueue(self, val):
		self.queue[self.init_idx + self.size] = val
		self.size += 1

	def dequeue(self):
		if self.size == 0:
			raise Exception("Can't dequeue on an empty Queue!")
		
		# Retrieve the first value using init_idx and update it
		first_val = self.queue.pop(self.init_idx)
		self.init_idx += 1
		self.size -= 1
		return first_val
		
	def peek(self):
		if self.size == 0:
			print("Empty Queue!")
			return
		return self.queue[self.init_idx]


if __name__ == '__main__':
	myQueue = Queue()
	myQueue.enqueue(1)
	myQueue.enqueue(2)
	myQueue.enqueue(3)
	print(myQueue)	# <- Front 1 2 3 End
	print(myQueue.init_idx)		# 0


	print(myQueue.peek())		# 1
	print(myQueue.dequeue())	# 1
	print(myQueue.init_idx)		# 1
	myQueue.enqueue(5)
	print(myQueue)			# <- Front 2 3 5 End	

	while myQueue:
		print(myQueue.dequeue())	# 2 3 5

	print("Below shows the result of dequeue on empty Queue")
	myQueue.dequeue()	# Error "Can't dequeue from an empty Queue"
