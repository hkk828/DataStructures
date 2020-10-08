from LinkedList import *

class OrderedLinkedList(LinkedList):
	
	# Overriding a method from LinkedList so that the values are ordered
	def append(self, val):
		if len(self) == 0:
			self.head = ListNode(val)
		else:
			# 'cursor' loops over the list, 'prev' is the previous node,
			# and 'found' checks whether a value bigger than val is found 
			prev = None
			cursor = self.head
			while cursor:
				if cursor.val > val:
					break
				prev = cursor
				cursor = cursor.get_next()
				
			new_node = ListNode(val, cursor)
			# val should be appended in front if it is the smallest
			# self.head is changed to the 'val'
			if prev == None:
				self.head = new_node
			# val is appended on other than the front. It can be added at the end.
			else:
				prev.set_next(new_node)
		self.size += 1


if __name__ == '__main__':
	l = OrderedLinkedList()
	l.append(9)
	l.append(7)
	l.append(1)
	l.append(5)
	l.append(3)
	print(l)	# head-> 1-> 3-> 5-> 7-> 9

	from random import randint
	messy = LinkedList()
	for i in range(10):
		messy.append(randint(0, 1000))
	print(messy)	# head-> ... random values in [0, 1000]
	
	# function that sorts a unordered LinkedList using OrderedLinkedList data structure
	def sort_list(l: LinkedList) -> LinkedList:
		temp = OrderedLinkedList()
		cursor = l.head
		while cursor:
			temp.append(cursor.get_value())
			cursor = cursor.get_next()
		sorted = LinkedList()
		cursor = temp.head
		while cursor:
	        	sorted.append(cursor.get_value())
	        	cursor = cursor.get_next()
		return sorted
	print(sort_list(messy))	# head-> ... sorted messy


