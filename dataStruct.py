#coding:utf-8

class LinkNode:
	def __init__(self,val):
		self.val = val
		self.next = None

#读链表返回数组
def read(node):
    n = []
    while node:
        n.append(node.val)
        node = node.next
    return n

#根据数组创建链表
def createNode(seq):
    head = a = ListNode(None)
    for i in seq:
        a.next = ListNode(i)
        a = a.next
    return head.next

#二叉树
class bTree:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None
#二叉查找树
class BST():
    def __init__(self):
        self.clear()

    def clear(self):
        self.root = None
        self.count = 0
    def insert(self,val):
    	if not val:
    		return
    	self.root = insert(self.root,val)
    	self.count += 1

    def delete(self,val):
    	self.root = delete(self.root,val)
    	self.count -= 1
    def isEmpty(self):
    	return not root
    def size(self):
    	return self.count
    def contains(self,val):
    	return search(self.root,val) != None

def search(ref,val):
	if not ref:
		return None
	else:
		if ref.data==val:
			return ref
		elif ref.data<val:
			search(ref.right,val)
		else:
			search(ref.left,val)
def insert(ref,val):
	if not ref:
		return bTree(val)
	else:
		if ref.data<val:
			ref.right = insert(ref.right,val)
		else:
			ref.left = insert(ref.left,val)
	return ref

def delete(ref,val):
	if ref:
		if ref.data == val:
			return deleteTop(ref);
		elif ref.data>val:
			ref.left = delete(ref.left,val)
		else:
			ref.right = delete(ref.right,val)
	return ref

def deleteTop(ref):
	if not ref.left:
		return ref.right
	elif not ref.right:
		return ref.left
	else:
		ref.data = getLeftmost(ref.right)
		ref.right = deleteLeftmost(ref.right)
		return ref

def getLeftmost(ref):
	while ref.left:
		ref = ref.left

	return ref.data
def deleteLeftmost(ref):
	if not ref.left:
		return ref.right
	else:
		ref.left = deleteLeftmost(ref.left)
		return ref

#前序遍历
def preOrder(ref):
    if not ref:
        return
    print ref.data,
    preOrder(ref.left)
    preOrder(ref.right)
#中序遍历
def inOrder(ref):
    if not ref:
        return 
    inOrder(ref.left)
    print ref.data,
    inOrder(ref.right)
#后序遍历
def postOrder(ref):
    if not ref:
        return
    return postOrder(ref.left)
    return postOrder(ref.right)
    print ref.data

#逆中序遍历
def reverseOrder(ref, level):
	if not ref:
		return
	reverseOrder(ref.right,level + 1)
	for i in xrange(level):
		print '    '
	print ref.data,
	reverseOrder(ref.left,level+1)

def createBackbone(root):
	if root:
		root.right = createBackbone(root.right)
		if root.left:
			oldRoot = root
			ref = root = createBackbone(root.left)
			oldRoot.left = None
			while ref.right:
				ref = ref.right
			ref.right = oldRoot
	return root
def createTree(root,n):
	if (n>2):
		m = (n - 1) /2
		oldRoot = root
		ref = root
		for i in xrange(1,m):
			ref = ref.right
		root = ref.right
		ref.right = None
		root.left = createTree(oldRoot,m)
		root.right = createTree(root.right,n - m - 1)

	return root

a = bTree(1)
a.left = bTree(2)
a.right = bTree(3)
a.left.left = bTree(4)
a.left.right = bTree(5)
a.right.left = bTree(6)
#preOrder(a)
#inOrder(a)
#reverseOrder(a,3)

class Solution(object):
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        seq = []
        self.pathSumHelp(root,sum,seq)
        
        return self.result
    
    def pathSumHelp(self, root, sum, seq):
        if not root:
            return
        
        if root.left == None and root.right == None:
            if root.data == sum:
                self.result.append(seq[:] + [root.data])
                return 
            else:
                return
        
        self.pathSumHelp(root.left,sum - root.data,seq[:].append(root.data))
        self.pathSumHelp(root.right,sum - root.data,seq[:].append(root.data))
s = Solution()
s.pathSum(a,13)
