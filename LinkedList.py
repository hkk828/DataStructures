class ListNode:
	
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def get_value(self):
		return self.val
	
	def set_value(self, new_value):
		self.val = new_value

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0
		# We can even introduce self.tail to keep track of the tail of the LinkedList
		# Using self.tail we can make append method run on constant time

	def __len__(self):
		return self.size

	# represent LinkedList as "Head-> a-> b-> c-> d"
	def __repr__(self):
		repr_str = "Head-> "
		cursor = self.head
		while cursor:
			val = cursor.val
			repr_str += str(val) + "-> "
			cursor = cursor.next
		return repr_str.rstrip("-> ")	# Removes "-> " at the end if it exists

	def append(self, val):
		if self.size == 0:
			self.head = ListNode(val)
		else:
			cursor = self.head
			# loop until cursor has no next
			while cursor.next:
				cursor = cursor.next
			cursor.set_next(ListNode(val))
		self.size += 1

	# find positions of Nodes having the same value as "val",
	# and return them as LinkedList
	def find(self, val):
		pos_list = LinkedList()
		
		idx = 0
		cursor = self.head
		while cursor:
			if cursor.val == val:
				pos_list.append(idx)
			cursor = cursor.next
			idx += 1
		return pos_list

	# delete value at position=idx
	def pop(self, idx=-1):
		if self.size == 0:
			raise Exception("Can't pop from an empty LinkedList!")

		# idx can be -self.size, (-self.size+1), ..., 0, 1, 2, ... (self.size-1)
		if idx < 0:
			idx += self.size
		# Now idx is one of 0, 1, 2, ..., (self.size-1)
		if (idx >= self.size) or (idx < 0):
			raise Exception("List index out of range!")
		
		if idx == 0:
			pop_value = self.head.val
			self.head = self.head.next
		else:
			# cursor will be at pos=(idx-1) after for-loop
			cursor = self.head
			for i in range(idx-1):
				cursor = cursor.next
			pop_value = cursor.next.val
			cursor.next = cursor.next.next
		
		self.size -= 1
		return pop_value
		
	# delete the first occurrence of value=val, otherwise return None
	def remove(self, val):
		cursor = self.head
		prev = None
		found = False
		while cursor:
			if cursor.val == val:
				found = True
				break
			prev = cursor
			cursor = cursor.next
	
		if not found:
			return

		# When removing the first value
		if prev == None:
			self.head = self.head.next
		# When removing a value which is not the first
		else:
			prev.next = cursor.next
		self.size -= 1

	def __getitem__(self, idx):
		if idx < 0:
			idx += self.size
		if (idx >= self.size) or (idx < 0):
			raise Exception("List index out of range!")
	
		cursor = self.head
		for i in range(idx):
			cursor = cursor.next
		return cursor.get_value()
	
	def __setitem__(self, idx, val):
		if idx < 0:
			idx += self.size
		if (idx >= self.size) or (idx < 0):
			raise Exception("List index out of range!")

		cursor = self.head
		for i in range(idx):
			cursor = cursor.next
		cursor.set_value(val)


if __name__ == '__main__':
	myList = LinkedList()
	for i in range(1, 6):
		myList.append(i)
	
	print(myList)	# Head-> 1-> 2-> 3-> 4-> 5
	print(f'Length of the list: {len(myList)}')	# 5
	
	myList.remove(3)
	print(myList)	# Head-> 1-> 2-> 4-> 5
	myList.append(2)
	print(myList.find(2))	# Head-> 1-> 4

	myList.remove(2)
	print(myList)	# Head-> 1-> 4-> 5-> 2

	print(myList.pop(1))	# 4
	print(myList.pop())	# 2
	
	print(myList)	# Head-> 1-> 5
	
	print(myList[1])# 5
	myList[1] = 2
	print(myList)	# Head-> 1-> 2
	





