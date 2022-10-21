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


# def pre_order(root):
#     # root, left, right
#     # 0 1 3 5 6 7 2 4
#     print(root.v, end=" ")
#     if root.left is not None:
#         pre_order(root.left)

#     if root.right is not None:
#         pre_order(root.right)


# def post_order(root):
#     # left, right, root
#     # 6 7 5 3 1 4 2 0
#     if root.left is not None:
#         post_order(root.left)

#     if root.right is not None:
#         post_order(root.right)
#     print(root.v, end=" ")


# def in_order(root):
#     # left, root, right
#     # 3 6 5 7 1 0 2 4
#     if root.left is not None:
#         in_order(root.left)
#     print(root.v, end=" ")
#     if root.right is not None:
#         in_order(root.right)


def pre_order(root, r=[]):
    # root, left, right
    # 0 1 3 5 6 7 2 4
    r.append(root.v)
    if root.left is not None:
        pre_order(root.left, r)

    if root.right is not None:
        pre_order(root.right, r)


def post_order(root, r=[]):
    # left, right, root
    # 6 7 5 3 1 4 2 0
    if root.left is not None:
        post_order(root.left, r)

    if root.right is not None:
        post_order(root.right, r)
    r.append(root.v)


def in_order(root, r=[]):
    # left, root, right
    # 3 6 5 7 1 0 2 4
    if root.left is not None:
        in_order(root.left, r)
    r.append(root.v)
    if root.right is not None:
        in_order(root.right, r)


r1, r2, r3 = [], [], []
pre_order(nodes[0], r1)
post_order(nodes[0], r2)
in_order(nodes[0], r3)
print(r1, r2, r3)
