import random

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.length = 0


	def insert_start(self,data):
		self.length +=1
		new_node = Node(data)

		if self.head == None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node


	def insert_end(self,data):
		if(self.length==0):
			raise Exception('len is 0, cannot insert at end')
		new_node = Node(data)

		old_head = self.head
		
		while (old_head.next is not None):
			old_head = old_head.next

		old_head.next = new_node
		self.length +=1


	def print(self):
		ptr_node = self.head

		while (ptr_node.next is not None):
			print(ptr_node.data)
			ptr_node = ptr_node.next
		print(ptr_node.data)


	def __str__(self):
		out = ''
		ptr_node = self.head
	
		while(ptr_node.next is not None):
			out += str(ptr_node.data)
			out += ','
			ptr_node = ptr_node.next
	
		out += str(ptr_node.data)
		return out


	def __len__(self):
		return self.length


	def populate(self,size,low=0.0,high=1.0,fx=float):
	
		for i in range(0,size):
			self.insert_start(fx(random.uniform(low,high)))

	
	def find_item(self,data):
		if self.head.data == data:
			return (0,data)
		ptr_node = self.head
		n = 0
		while(ptr_node.next != None):
			ptr_node = ptr_node.next
			n+=1
			if (ptr_node.data == data):
				return (n,data)
		return None

	def traverse_index(self,index,fx=None):
		if (index > self.length or index < 0):
			return None
		ptr_node = self.head
		prev_ptr_node = None
		for i in range(0,index):
			prev_ptr_node = ptr_node
			ptr_node = ptr_node.next
		if (fx != None):
			ptr_node.data = fx(ptr_node.data)
		return (prev_ptr_node,ptr_node)

	def remove_index(self,index):
		fetched_pair = self.traverse_index(index)
		if (index == 0):
			self.head = self.head.next
			self.length-=1
			return (index,fetched_pair[1].data)
		if (index == self.length):
			fetched_pair[0].next = None
			self.length -=1
			return (index,fetched_pair[1].data)
		if (index > self.length):
			print('index exceedes length!')
			return None
		fetched_pair[0].next = fetched_pair[1].next
		fetched_pair[1].next = None
		self.length-=1
		return (index,fetched_pair[1].data)

		

			
