from collections import deque

# 节点类
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

# 树类
class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    # 添加节点
    def add(self, elem):
        node = Node(elem)

        # 若根节点的值为-1，即此时树是空
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            # 若根节点的值不为-1，则当前节点为list中的第一个
            treeNode = self.myQueue[0]
            # 若左儿子为None
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            # 右儿子为None
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                # pop出list中第一个节点，准备下一次赋值
                self.myQueue.pop(0)

    # 递归实现遍历
    # 前序遍历
    def preOrderTravelRecursion(self, root):
        if root == None:
            return
        print(root.elem, end=' ')
        self.preOrderTravelRecursion(root.lchild)
        self.preOrderTravelRecursion(root.rchild)

    # 中序遍历
    def inOrderTravelRecursion(self, root):
        if root == None:
            return
        self.inOrderTravelRecursion(root.lchild)
        print(root.elem, end=' ')
        self.inOrderTravelRecursion(root.rchild)

    # 后序遍历
    def postOrderTravelRecursion(self, root):
        if root == None:
            return
        self.postOrderTravelRecursion(root.lchild)
        self.postOrderTravelRecursion(root.rchild)
        print(root.elem, end=' ')

    # 栈实现遍历
    # 前序遍历
    def preOrderTravelStack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.elem, end=' ')
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    # 中序遍历
    def inOrderTravelStack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print(node.elem, end=' ')
            node = node.rchild

    # 后序遍历
    def postOrderTravelStack(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            print(myStack2.pop().elem, end=' ')

    # 广度优先遍历
    def levelOrderTravelStack(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem, end=' ')
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)

    def levelOrderTravelQueue(self, root):
        if root == None:
            return
        q = deque()
        node = root
        q.append(node)
        while q:
            node = q.popleft()
            print(node.elem, end=' ')
            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)


if __name__ == '__main__':
    tree = Tree()
    for elem in range(10):
        tree.add(elem)

    print("Pre-order travel by Recursion:")
    tree.preOrderTravelRecursion(tree.root)
    print("\n")
    print("In-order travel by Recursion:")
    tree.inOrderTravelRecursion(tree.root)
    print("\n")
    print("Post-order travel by Recursion:")
    tree.postOrderTravelRecursion(tree.root)
    print("\n")

    print("Pre-order travel by Stack:")
    tree.preOrderTravelStack(tree.root)
    print("\n")
    print("In-order travel by Stack:")
    tree.inOrderTravelStack(tree.root)
    print("\n")
    print("Post-order travel by Stack:")
    tree.postOrderTravelStack(tree.root)
    print("\n")

    print("Level-order travel by Stack:")
    tree.levelOrderTravelStack(tree.root)
    print("\n")

    print("Level-order travel by Dequeue:")
    tree.levelOrderTravelQueue(tree.root)