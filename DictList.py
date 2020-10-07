class DictList:
	'''
	DictList is implemented with python dictionary.
	Because the python dictionary uses hashtable concept,
	DictList append, pop, and __getitem__ can be done in constant time. 
	'''
	
	def __init__(self):
		self.list = {}
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def append(self, val):
		self.list[self.size] = val
		self.size += 1

	def pop(self, idx=-1):
		# When a DictList is empty, then raise an Error
		if self.size == 0:
			raise Exception("No item to pop!")
		# if idx < 0 -> idx += self.size
		if idx < 0:
			idx += self.size
		# if idx >= self.size or idx < 0 -> index error
		if (idx >= self.size) or (idx < 0):
			raise Exception("List index out of range!")

		pop_value = self.list[idx]
		# Shifting all the values after "idx" to the left
		for j in range(idx, self.size-1):
			self.list[idx] = self.list[idx+1]
		
		# Delete the last item
		del self.list[self.size-1]
		self.size -= 1
		return pop_value

	def find(self, val):
		pos = ()
		for idx in range(self.size):
			if val == self.list[idx]:
				pos += (idx,)
		return pos

	def __getitem__(self, idx):
		# idx can be -self.size, ..., 0, 1, 2, ... (self.size-1), where -k returns the k-th element from the end
		if idx < 0:
			idx += self.size
		return self.list[idx]

	def __setitem__(self, key, val):
		if idx < 0:
			idx += self.size
		self.list[key] = val	

	def __repr__(self):
		# Represent DictList as "[ ]" when empty, and "a-> b-> c-> d" when it contains a, b, c, and d in order.
		if self.size == 0:
			return "[ ]"
		repr_form = str(self.list[0])
		for idx in range(1, self.size):
			repr_form += "-> " + str(self.list[idx])
		return repr_form

	def toDictList(self, pyList):
		# Build a DictList from a python list
		for idx, val in enumerate(pyList):
			self.list[(self.size + idx)] = val
		self.size += len(pyList)

	def extend(self, other):
		# Extend self with putting other DictList at the end
		for idx in range(len(other)):
			self.list[(self.size + idx)] = other[idx]
		self.size += len(other)
		return self

	def __add__(self, other):
		# implements "+" operation. E.g., "1-> 2" + "3-> 4" = "1-> 2-> 3-> 4"	
		return self.extend(other)




if __name__ == '__main__':
	myList = DictList()
	for i in range(3, 10):
		myList.append(i)
	print(myList)	# "3-> 4-> 5-> 6-> 7-> 8-> 9"
	print(myList.pop()) # 9
	print(myList.find(8))	# (5,)
	myList.append(8)
	print(myList)	# "3-> 4-> 5-> 6-> 7-> 8-> 8"
	print(myList.find(8)) # (5, 6)
	print(myList[1]) # 4
	print(myList[-1]) # 8
	
	pyList = [1, 2]
	newList = DictList()
	newList.toDictList(pyList)
	print(newList) # "1-> 2"

	print(newList.extend(myList)) # "1-> ... -> 8-> 8"
	
	otherList = DictList()
	otherList.toDictList([1, 2])
	print(otherList + myList) # "1-> ... -> 8-> 8"

