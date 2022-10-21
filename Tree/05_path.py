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
root = nodes[0]
# lca with data_structure.parent


def all_path(root):
    def dfs(node, path, ret):
        if node.left is None and node.right is None:
            ret.append(path)
        if node.left is not None:
            dfs(node.left, path+f"->{node.left.v}", ret)
        if node.right is not None:
            dfs(node.right, path+f"->{node.right.v}", ret)
    ret = []
    if root is not None:
        dfs(root, str(root.v), ret)
    return ret


def all_path_my(root):
    def dfs(node, path, ret):
        if node.left is None and node.right is None:
            path_str = "->".join([str(i.v) for i in path])
            ret.append(path_str)
        if node.left is not None:
            path.append(node.left)
            dfs(node.left, path, ret)
            path.pop()
        if node.right is not None:
            path.append(node.right)
            dfs(node.right, path, ret)
            path.pop()
    ret = []

    if root is not None:
        path = [root]
        dfs(root, path, ret)
    return ret


print(all_path(root))
print(all_path_my(root))

def goodnode(root):
    '''
    这道题，maxv是从上往下传，不需要更新，直接用参数传就可以，想一下递归过程调用的原理
    用一个全局的来统计res个数
    '''
    res=0
    def func(node,maxv):
        if node is None:
            return
        nonlocal res
        if maxv<= node.v:
            res+=1
        func(node.left,max(maxv,node.v))
        func(node.right,max(maxv,node.v))
    func(root,root.v)
    return res

'''
1148 leecode
        3
    1       4
  3       1    5
'''
nodes = [TreeNode(i) for i in range(9)]
nodes[0].add_left(nodes[1])
nodes[0].add_right(nodes[2])
nodes[0].v=3
nodes[2].v=4

nodes[1].add_left(nodes[3])

nodes[2].add_left(nodes[4])
nodes[4].v=1
nodes[2].add_right(nodes[5])
nodes[5].v=5
root = nodes[0]
print(goodnode(root))


def maxPathSum(root:TreeNode) -> int:
    '''
    这道题比较难的是：人字形的怎么处理
    从上到下的maxv,我们都知道怎么处理
    难点在于：它用一个值来记录maxv,另外return只return一边（还只考虑非负数的情况）
    这道题我自己想不出来，尽管答案很简洁
    '''
    maxv = root.v
    def func(node):
        nonlocal maxv
        if node is None:
            return 0
        left = max(0,func(node.left))
        right = max(0,func(node.right))
        maxv = max(maxv,left+right+node.v)
        return max(left,right)+ node.v
    func(root)
    return maxv
nodes = [TreeNode(i+1) for i in range(3)]
nodes[0].add_left(nodes[1])
nodes[0].add_right(nodes[2])
print(maxPathSum(nodes[0]))

def func_1120(root):
    mavg = root.v
    def func(node):
        if node is None:
            return 0,0
        asum1,num1 = func(node.left)
        asum2,num2 = func(node.right)
        asum = asum1 + asum2 + node.v
        num = num1+num2+1
        mavg = max(mavg,asum/num)
        return asum, num
    func(root)
    return mavg
