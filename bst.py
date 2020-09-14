import random


class Node:

	def __init__(self, data):
		self.data=data
		self.left = None
		self.right = None


class bst:

	
	
	def __init__(self, data):
		self.root = Node(data)
		#self.inorder = []
	
	def insert(self,new_node,rel_node=None):
		if(rel_node == None):
			rel_node = self.root
		if new_node.data >= rel_node.data:
			if rel_node.right != None:
				self.insert(new_node,rel_node.right)
			else:
				rel_node.right = new_node
				return 'inserted'

		if new_node.data <= rel_node.data:
			if rel_node.left != None:
				self.insert(new_node,rel_node.left)
			else:
				rel_node.left = new_node
				return 'inserted'


	def inorder(self,rel_root=None):
		if rel_root == None:
			rel_root = self.root

		if(rel_root.left):
			self.inorder(rel_root.left)
		print(rel_root.data)
		if(rel_root.right):
			self.inorder(rel_root.right)


		
		
	def delete(self,del_node,rel_root=None):
		if rel_root == None:
			rel_root = self.root

		if del_node.data > rel_root.data:
			
			pass

	def get_max(self,rel_node=None):
		if rel_node == None:
			rel_node = self.root

		if(rel_node.right != None):
			return (self.get_max(rel_node.right))
		else:
			return rel_node.data

	def get_min(self,rel_node=None):
		if rel_node == None:
			rel_node = self.root

		if(rel_node.left != None):
			return (self.get_min(rel_node.left))
		else:
			return rel_node.data

	def find_node(self,qdata,rel_node = None,parent_node = None):
		if rel_node == None:
			rel_node = self.root

		if(qdata > rel_node.data):
			if(rel_node.right == None):
				return None
			else:
				return (self.find_node(qdata,rel_node.right,parent_node = rel_node))
		elif(qdata < rel_node.data):
			if(rel_node.left == None):
				return None
			else:
				return (self.find_node(qdata,rel_node.left,parent_node = rel_node))
		elif(qdata == rel_node.data):
			return [rel_node,parent_node]
		else:
			return None
			

	def populate(self,size,low=0.0,high=1.0,fx=float):
		for i in range(0,size):
			self.insert(Node(fx(random.uniform(low,high))))
		
		
	def predecessor(self,rel_node=None):
		if (rel_node == None):
			rel_node = self.root.left
		else:
			myself = rel_node
			rel_node = rel_node.left
		

		if(rel_node == None):
			return myself	

		prev = None
	
		while(rel_node.right != None):
			prev = rel_node		
			rel_node = rel_node.right

		return [rel_node,prev]
			

	def delete_node(self,rel_node,parent):
		
		if rel_node.right and not rel_node.left:
			if parent.data > rel_node.data:
				parent.left = rel_node.right
			elif parent.data < rel_node.data:
				parent.right = rel_node.right
			del rel_node
			return 'deleted node with child(R)'
		
		elif rel_node.left and not rel_node.right:
			if parent.data > rel_node.data:
				parent.left = rel_node.left
			elif parent.data < rel_node.data:
				parent.right = rel_node.left
			del rel_node
			return 'deleted node with child(L)'

		elif rel_node.right and rel_node.left:
#			breakpoint()
			pre = self.predecessor(rel_node)
			tmp = rel_node.data
			rel_node.data = pre[0].data
			return self.delete_node(pre[0],pre[1])

		elif not rel_node.right and not rel_node.left:
			if parent.data > rel_node.data:
				parent.left = None
			if parent.data < rel_node.data:
				parent.right = None
			del rel_node
			return 'deleted leaf node'
			
		


a = bst(50)
a.populate(10,fx=lambda x: int(x*100))
a.inorder()
