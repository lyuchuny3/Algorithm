class TreeNode:
    def __init__(self, v, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.v = v
        self.parent = -1

    def add_left(self, l):
        self.left = l
        l.parent = self

    def add_right(self, r):
        self.right = r
        r.parent = self

    def __repr__(self):
        return f"{self.v}({self.left},{self.right})"


'''
        0
    1       2
3               4
   5
  6  7
'''
nodes = [TreeNode(i) for i in range(8)]
nodes[0].add_left(nodes[1])
nodes[0].add_right(nodes[2])
nodes[1].add_left(nodes[3])
nodes[2].add_right(nodes[4])
nodes[3].add_right(nodes[5])
nodes[5].add_left(nodes[6])
nodes[5].add_right(nodes[7])


# root, left, right
# 0 1 3 5 6 7 2 4
def preorder(root):
    assert root is not None
    ret = []
    stack = [root]
    while len(stack) != 0:
        n = stack.pop()
        ret.append(n.v)
        if (n.right is not None):
            stack.append(n.right)
        if (n.left is not None):
            stack.append(n.left)
    return ret
    assert ret == [0, 1, 3, 5, 6, 7, 2, 4]
    print(ret)


def post_order(root):
    assert root is not None
    ret = []
    stack = [root]
    while len(stack) != 0:
        n = stack.pop()
        ret.append(n.v)
        if n.left is not None:
            stack.append(n.left)
        if n.right is not None:
            stack.append(n.right)
    print(ret[::-1])
    assert (ret[::-1] == [6, 7, 5, 3, 1, 4, 2, 0])


'''
    DFS:pre-order
    root,left,right
    stack in python: list (append, pop)
      append(root,right,left)
      pop: root,left,right
use this to think in mind the stack order
    1
   2 5
  3 4
'''


def in_order(root):
    '''
    util deep left is None, 才 root.add to ret,
    then right
    '''
    ret = []
    stack = []
    node = root
    while len(stack) != 0 or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        ret.append(node.v)
        node = node.right
    print(ret)
    assert (ret == [3, 6, 5, 7, 1, 0, 2, 4])


preorder(nodes[0])
post_order(nodes[0])
in_order(nodes[0])
