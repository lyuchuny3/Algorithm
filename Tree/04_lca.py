class TreeNode:
    def __init__(self, v, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.v = v
        self.parent = None
        self.depth = 0

    def add_left(self, l):
        self.left = l
        l.parent = self

    def add_right(self, r):
        self.right = r
        r.parent = self

    def __repr__(self):
        return f"{self.v}({self.left},{self.right})"

    def lca(self, a, b):
        def traverse(node):
            ret = []
            p = node.parent
            while (p is not None):
                ret.append(p)
                p = p.parent
            return ret
        la = traverse(a)
        bp = b.parent
        while bp not in la:
            bp = bp.parent
        return bp


'''
        0
    1       2
  3            4
8   5
  6  7
'''
nodes = [TreeNode(i) for i in range(9)]
nodes[0].add_left(nodes[1])
nodes[0].add_right(nodes[2])
nodes[1].add_left(nodes[3])
nodes[2].add_right(nodes[4])
nodes[3].add_right(nodes[5])
nodes[5].add_left(nodes[6])
nodes[5].add_right(nodes[7])
nodes[3].add_left(nodes[8])

# lca with data_structure.parent


def test_lca():
    assert nodes[0].lca(nodes[8], nodes[7]) == nodes[3]
    assert nodes[0].lca(nodes[6], nodes[4]) == nodes[0]

# lca recursize (p,q)


def lca(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    if root is None:
        return root
    if root in [p, q]:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    if right is not None:
        return right

# lca dfs_parent (p,q)


def lca_2(root, p, q):
    # dfs get parent
    parent = {}

    def traverse(p, node):
        if node is not None:
            parent[node] = p
        if node.left is not None:
            traverse(node, node.left)
        if node.right is not None:
            traverse(node, node.right)
    traverse(None, root)
    # 需要考虑包不包括自身
    la = []
    while p is not None:
        la.append(p)
        p = parent[p]

    while q not in la:
        q = parent[q]
    return q

# lca recursive (multi)


def lca_3(root, nodes):
    def dfs(root, nodes):
        if root is None:
            return root
        if root.v in nodes:
            return root
        left = dfs(root.left, nodes)
        right = dfs(root.right, nodes)
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None
    return dfs(root, nodes).v


'''
        0
    1       2
  3            4
8   5
  6  7
'''
print(lca_3(nodes[0], [3, 7, 6]))

# lca_4: 1123 lca of deepest leaves
# my implementation


def lca_4(root):

    max_depth = -1

    def deepest_node(node, ret, depth):
        nonlocal max_depth
        if node is not None:
            if depth >= max_depth:
                if depth > max_depth:
                    max_depth = depth
                    ret.clear()
                ret.append(node)
        if node.left is not None:
            deepest_node(node.left, ret, depth+1)
        if node.right is not None:
            deepest_node(node.right, ret, depth+1)

    ret = []
    deepest_node(root, ret, 0)

    def lca(root, nodes):
        if root is None:
            return None
        if root in nodes:
            return root
        left = lca(root.left, nodes)
        right = lca(root.right, nodes)
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
    return lca(root, ret)


print(lca_4(nodes[0]))

# ref implementation 1123


def lca_deep(root):
    def get_lca(node, depth):
        if node is None:
            return node, depth
        left, dl = get_lca(node.left, depth+1)
        right, dr = get_lca(node.right, depth+1)
        if dl == dr:
            return node, dl
        if dl > dr:
            return left, dl
        else:
            return right, dr
    node, depth = get_lca(root, 0)
    return node


print(lca_deep(nodes[0]))
