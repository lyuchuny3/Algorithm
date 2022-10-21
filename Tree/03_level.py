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


def level_order(root):
    ret = []
    queue = []
    if root is not None:
        queue.append(root)
    while len(queue) != 0:
        num = len(queue)
        level = []
        for i in range(num):
            n = queue.pop()
            level.append(n.v)
            if n.left is not None:
                queue.insert(0, n.left)
            if n.right is not None:
                queue.insert(0, n.right)
        ret.append(level)
    assert ret == [[0], [1, 2], [3, 4], [5], [6, 7]]
    return ret


print(level_order(nodes[0]))


def level_order_1(root):
    ret = []

    def dfs(node, ret, depth):
        if node is None:
            return
        if len(ret) == depth:
            ret.append([])
        ret[depth].append(node.v)
        if node.left is not None:
            dfs(node.left, ret, depth+1)
        if node.right is not None:
            dfs(node.right, ret, depth+1)
    dfs(root, ret, 0)
    assert ret == [[0], [1, 2], [3, 4], [5], [6, 7]]
    return ret


print(level_order_1(nodes[0]))


def vertical_order(root):
    hashmap = {}

    def dfs(node, ret, curr_offset):
        if node is None:
            return
        if curr_offset not in hashmap:
            hashmap[curr_offset] = []
        hashmap[curr_offset].append(node.v)
        if node.left is not None:
            dfs(node.left, hashmap, curr_offset-1)
        if node.right is not None:
            dfs(node.right, hashmap, curr_offset+1)
    dfs(root, hashmap, 0)

    ret = sorted(hashmap.items(), key=lambda x: x[0])
    return [i[1] for i in ret]


def vertical_order_1(root):
    ret = {}
    node_to_col = {}
    queue = []
    if root is not None:
        queue.append(root)

    node_to_col[root] = 0
    minv = 0
    while len(queue) != 0:
        num = len(queue)
        for i in range(num):
            n = queue.pop()
            col = node_to_col[n]
            minv = min(col, minv)
            if col not in ret:
                ret[col] = []
            ret[col].append(n.v)

            if n.left is not None:
                queue.insert(0, n.left)
                node_to_col[n.left] = col-1

            if n.right is not None:
                queue.insert(0, n.right)
                node_to_col[n.right] = col+1
    out = []
    while minv in ret:
        out.append(ret[minv])
        minv += 1
    return out


print(vertical_order(nodes[0]))
print(vertical_order_1(nodes[0]))
