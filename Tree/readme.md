## code 1: recursive for Binary Tree Preorder,Inorder,Postorder Traversal
用recursive的写法写二叉树的pre,in,post-order是比较简单的


```
def pre_order(root, r=[]):
    # root, left, right
    r.append(root.v)
    if root.left is not None:
        pre_order(root.left, r)
    if root.right is not None:
        pre_order(root.right, r)

def post_order(root, r=[]):
    # left, right, root
    if root.left is not None:
        post_order(root.left, r)
    if root.right is not None:
        post_order(root.right, r)
    r.append(root.v)

def in_order(root, r=[]):
    # left, root, right
    if root.left is not None:
        in_order(root.left, r)
    r.append(root.v)
    if root.right is not None:
        in_order(root.right, r)

```
## code 2: iterative for Binary Tree Preorder,Inorder,Postorder Traversal
用iterative的方法写就比较有挑战了，这里列出的stack的pre,in,post-order的遍历。我个人比较喜欢pre,post的写法，比较简单，post和pre的区别是，post的ret是倒序加入的，可以用insert(0,elem），也可以最后再反序过来，in_order的思路是一条路走到黑，然后再append中间的，接着才是右边的
这本质就是回溯法了 （iterative)

```
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

def inorder(root):
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
   return ret


def postorder(root):
    assert root is not None
    ret = []
    stack = [root]
    while len(stack) != 0:
        n = stack.pop()
        ret.insert(0, n.v) ### inverse
        if n.left is not None:
            stack.append(n.left)
        if n.right is not None:
            stack.append(n.right)
   return ret

```
## code3: level order
- BFS直接iterative写是比较直观的，就一个queue，然后不断地加它的左右子节点到队列的尾巴
- DFS来写一层一层遍历的话，和preorder是类似的，先处理当前节点（在相应的深度添加当前节点），然后处理左右节点
```
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
    return ret


def level_order_1(root):
    ret = []
    def dfs(node, ret, depth):
        if node is None:
            return
        if len(ret) == depth:
            ret.append([])
        ret[depth].append(node.v) #	我一开始写错了，写成 ret[-1].append(node.v)，跟踪它的遍历顺序知道它不是一层一层遍历的，而是深度优先，需要找到对应的层写入结果）

        if node.left is not None:
            dfs(node.left, ret, depth+1)
        if node.right is not None:
            dfs(node.right, ret, depth+1)
    dfs(root, ret, 0)
```
