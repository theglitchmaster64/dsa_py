import random

class Node:

	def __init__(self,data,parent=None):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None
		self.height = 0

class avl:

	def __init__(self,data):
		self.root = Node(data,None)

	def insert(self,data,rel_root=None):
		if rel_root == None:
			rel_root = self.root

		if data > rel_root.data:
			if rel_root.right:
				self.insert(data,rel_root.right)
			else:
				rel_root.right = Node(data,rel_root)

		elif data < rel_root.data:
			if rel_root.left:
				self.insert(data,rel_root.left)
			else:
				rel_root.left = Node(data,rel_root)
		rel_root.height = max(self.calc_height(rel_root.left),self.calc_height(rel_root.right))+1
		self.handle_violation(rel_root)



	def remove_node(self,data,rel_root=None):
		if rel_root == None:
			rel_root = self.root

		if data > rel_root.data:
			self.remove_node(data,rel_root.right)
		elif data < rel_root.data:
			self.remove_node(data,rel_root.left)

		else:
			if rel_root.left is None and rel_root.right is None:
				parent = rel_root.parent
				if parent is not None and parent.left == rel_root:
					parent.left = None
				elif parent is not None and parent.right == rel_root:
					parent.right = None

				if parent is None:
					self.root = None

				del rel_root

				self.handle_violation(parent)
				return 'deleted leaf node'

			if rel_root.left is None and rel_root.right is not None:
				parent=rel_root.parent

				if parent is not None:
					if parent.left == rel_root:
						parent.left = rel_root.right
					elif parent.right == rel_root:
						parent.right = rel_root.right
				else:
					self.root = rel_root.right

				rel_root.right.parent = parent
				del rel_root
				self.handle_violation(parent)

				return 'deleted node with child (R)'


			elif rel_root.left is not None and rel_root.right is None:
				parent = rel_root.parent

				if parent is None:
					if parent.left == rel_root:
						parent.left = rel_root.left
					if parent.right == rel_root:
						parent.right = rel_root.left
				else:
					self.root = rel_root.left

				rel_root.left.parent = parent
				del rel_root
				self.handle_violation(parent)

				return 'deleted node with child (L)'

			else:
				pre = self.predecessor()
				tmp = pre.data
				pre.data = rel_root.data
				rel_root.data = tmp

				self.remove_node(data,pre)




	def predecessor(self,rel_root=None):
		if rel_root == None:
				rel_root = self.root.left
		else:
			rel_root = rel_root.left

		while(rel_root.right != None):
			rel_root = rel_root.right

		return rel_root


	def inorder(self,rel_root=None):
		if rel_root == None:
			rel_root = self.root

		if rel_root.left:
			self.inorder(rel_root.left)
		print(rel_root.data)
		if rel_root.right:
			self.inorder(rel_root.right)

	def calc_height(self,node):
		if node is None:
			return -1
		return node.height

	def calc_balance(self,node):
		if node is None:
			return 0
		else:
			return self.calc_height(node.left) - self.calc_height(node.right)

	def violation_helper(self,node):
		bal = self.calc_balance(node)
		if (bal > 1):
			if(self.calc_balance(node.left)<0):
				self.rotate_left(node.left)
			self.rotate_right(node)
		elif (bal < -1):
			if(self.calc_balance(node.right)>0):
				self.rotate_right(node.right)
			self.rotate_left(node)

	def handle_violation(self,node):
		while node is not None:
			node.height = max(self.calc_height(node.left),self.calc_height(node.right))+1
			self.violation_helper(node)
			node=node.parent

	def rotate_right(self,node):
		tmp_lnode = node.left
		tmpl_r = tmp_lnode.right

		tmp_lnode.right = node
		node.left = tmpl_r

		if tmpl_r is not None:
			tmpl_r.parent = node

		tmp_parent = node.parent
		node.parent = tmp_lnode
		tmp_lnode.parent = tmp_parent

		if tmp_lnode.parent is not None and tmp_lnode.parent.left == node:
			tmp_lnode.parent.left = tmp_lnode

		if tmp_lnode.parent is not None and tmp_lnode.parent.right == node:
			tmp_lnode.parent.right = tmp_lnode

		if node == self.root:
			self.root = tmp_lnode

		node.height = max(self.calc_height(node.left),self.calc_height(node.right))+1
		tmp_lnode.height = max(self.calc_height(tmp_lnode.left),self.calc_height(tmp_lnode.right))+1

	def rotate_left(self,node):
		tmp_rnode = node.right
		tmpr_l = tmp_rnode.left

		tmp_rnode.left = node
		node.right = tmpr_l

		if tmpr_l is not None:
			tmpr_l.parent = node

		tmp_parent = node.parent
		node.parent = tmp_rnode
		tmp_rnode.parent = tmp_parent

		if tmp_rnode.parent is not None and tmp_rnode.parent.left == node:
			tmp_rnode.parent.left = tmp_rnode

		if tmp_rnode.parent is not None and tmp_rnode.parent.right == node:
			tmp_rnode.parent.right = tmp_rnode

		if node == self.root:
			self.root = tmp_rnode

		node.height = max(self.calc_height(node.left),self.calc_height(node.right))+1
		tmp_rnode.height = max(self.calc_height(tmp_rnode.left),self.calc_height(tmp_rnode.right))+1
