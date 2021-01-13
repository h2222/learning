from random import randint, sample
"""
1. 把题目的要求细化，搞清楚根节点应该做什么，然后剩下的事情抛给前/中/后序的遍历框架就行了，
    我们千万不要跳进递归的细节里，你的脑袋才能压几个栈呀。
2. 

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def build_default_tree(self, node, ls = [1, 2, 3, 4, 5, 6, 7]):
        node.val = ls.pop(0)
        

"""
翻转二叉树, leetcode:226

"""
# 递归法, bfs思想, 前序遍历
def invert_binary_tree(node):
    if not node:
        return None
    node.right, node.left = node.left, node.right
    invert(node.left)
    invert(node.right)
    return node

# 迭代法, bfs思想, z字打印二叉树同款
def insert_binary_tree(node):
    queue = [node]
    while queue:
        q = queue.pop(0)
        q.left, q.right = q.right, q.left
        if q.left:
            queue.append(q.left)
        if q.right:
            queue.append(q.right)
    return node


"""
二叉树展开为链表, leetcode: 114
"""

# 递归法, 前序遍历
def flatten_binary_tree(node):
    pre_order_ls = []
    
    def pre_order(node): # 前序遍历
        if node:
            pre_order_ls.append(node)
            pre_order(node)
            pre_order(node)
    
    pre_order(node)
    size = len(pre_order_ls)
    for i in range(1, size):
        prev, curr = pre_order_ls[i-1], pre_order_ls[i]
        prev.left = None
        prev.right = curr


# 迭代法, 单栈法
def flatten_binary_tree(node):
    pre_order_ls = []
    stack = []
    while node or stack:
        while node:
            pre_order_ls.append(node)
            stack.append(node)  # go deeper, 往上叠
            node = node.left
        node = stack.pop(-1) # 从顶开始吐
        node = node.right # 吐出来的往右拐, 然后在往左go deeper

    size = len(pre_order_ls)
    for i in range(1, size):
        prev, curr = pre_order_ls[i-1], pre_order_ls[i]
        prev.left = None
        prev.right = curr    


"""
二叉树横向联通: connect LeetCode 116
二叉树加入新的属性next, 使用next对二叉树进行横向联通
        1
       / \
       2  3
     / \  / \
    4  5  6  7  
        1 ->
       / \
      2 -> 3 ->
     / \  / \
    4->5->6->7 -> Null
"""

setattr(TreeNode, 'next', None)
def left_connct(node):
    queue = [node]
    while queue: 
        head = queue[0]
        size = len(queue)
        for i in range(1, size): # 把在queue的element连起来
            head.next = queue[i] # 从1开始哈, 别忘了, head第一遍是0
            head = queue[i]     
        for _ in range(0, size):
            head = queue.pop(0) # 把已经连起来的element吐出来
            if head.left:
                queue.append(head.left) 
            if head.rightL:
                queue.append(head.right)



"""
二叉树层序遍历 nc 15
横向打印二叉树, 使用queue 进行区分
    3
   / \
  9  20
 / \ / \
15 7 N  N
output:
[[3], [9, 20], [15, 7]]
"""
def level_order(root):
    queue = [root]
    fina_res = []
    while queue:
        temp_res = []
        for _ in range(len(queue)):
            head = queue.pop(0)
            temp_res.append(head.val)
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)
        final_res.append(temp_res)
    return final_res


#######################################
"""
构建最大二叉树 leetcode 654
输出[3, 2, 1, 6, 0, 5]
找到list中最大的值, 然后利用最大值做部分和有部分中的最大值建立子子树
      6
    /   \
   3     5
  / \    / \
null 2  0   null
    /  \
  null  1
"""

def maximum_binary_tree(nums):
    if len(nums) == 0:
        return null  # 终止条件
    
    max_value = - float('inf')
    for i in nums:   # 找最大值
        max_value = max(max_value, i)

    root = TreeNode(max_value) # 建树    

    max_idx = nums.index(max_value) # 最大值引所
    left_part = nums[:max_idx] # 左右切分
    right_part = nums[max_idx+1:]

    root.left = maximum_binary_tree(left_part) # 前序遍历(遇到终止条件, 连接null)
    root.right = maximum_binary_tree(right_part)
    return root


"""
给出前序遍历和中序遍历, 还原二叉树 leetcode 105
给出后序遍历和中序遍历, 还原二叉树 leetcode 
"""

def build_tree(in_order, pre_order):

    if not(in_noder or pre_order):
        return None
    
    target = pre_order[0]
    root = TreeNode(target)
    in_index = pre_order.index(root.val)

    in_l_part = in_order[:in_index]
    in_r_part = in_order[in_index + 1:]
    pre_l_part = pre_order[1:in_index + 1] # 切分, 此处之一, 因为pre_order[0]为root点, 所用在取pre_order左右部分时需要顺延, 也就是 index+1
    pre_r_part = pre_order[ in_index + 1:]

    root.left = build_tree(in_l_part, pre_l_part)
    root.right = build_tree(in_r_part, pre_r_part)
    return root

    
"""
计算二叉树的节点数 leetcode 222
"""

def count_binary_tree(root): # 后序遍历加计数
    if not root: # 因为左右没有节点数目了
        return 0
    left_ct = count_binary_tree(root.left)
    right_ct = count_binary_tree(root.right)
    coutn = right_ct + left_connct + 1
    return count


"""
计算二叉树最大深度 leetcode 55
"""
def max_deep_tree(root):
    if not root:
        return 0
    left_deep = max_deep_tree(root.left)
    right_deep = max_deep_tree(root.right)
    deep = max(left_deep, right_deep) + 1
    return deep



"""
计算二叉树的重复子树 leetcode 652
本题考查二叉树的前/中/后序遍历的选择, 和如何序列化二叉树
"""

def find_duplicate_sub_tree(root):
    count_sub_tree = {} # 对子树进行计数
    save_dup_tree = {}  # 保存重复的子树
    def find(root):
        if not root:
            return "没子树了"
        left_str = find(root.left) # 后序遍历(因为要扫描掉整颗树才能知道有没有重复)
        right_str = find(root.right)
        sub_tree_str = left_str + "," + right_str + "," + str(root.val) # 二叉树序列化
        count_binary_tree.setdefault(sub_tree_str, 1) # 初始化
        if count_binary_tree[sub_tree_str] == 2:
            save_dup_tree.append(root) # 保存重复的子树
        count_binary_tree[sub_tree_str] += 1
        return sub_tree_str
    
"""
实现二叉树， 前中后序遍历 nc45
"""
def three_find(root):
    pre, ino, pos = [], [], []
    def find(root):
        if not root:
            return None
        pre.append(root.val)
        find(root.left)
        ino.append(root.val)
        find(root.right)
        pos.append(root.val)
    find(root)
    res = [pre, ino, pos]
    return res


"""
构建二叉搜索树:BST(binary search tree)
BST: 根节点的值小于左节点的值, 根节点的值小于右节点的值, 且左右节点均为二叉搜索树
"""

# 构建单颗bst, mid 直接求中间值就可以
def build_bst(start, end):
    if not root:
        return
    mid = (start + end) // 2
    root = TreeNode(mid)
    build(start, mid - 1)
    build(mid + 1, end)
    return root

# 构建多颗bst, 需要动态的调整i的位置以达到构建多颗bst的目的




"""
找到搜索二叉树(BST)的最近公共祖先 leetcode offer 68 |
解析: 
1. 清楚BST的性质, 即root.val > root.left.val, root.val < root.left.val, 且 root.left 与 root.right 也为搜索二叉树
2. 空树 (None tree) 也是树!
3. 总体思路为前序遍历, 分为递归和非递归2种实现
"""

# dsf - preorder - recursion
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    if root.val < q.val and root.val < p.val: # p q的 val 比 root 的 val 都要大, 说明root需要右移增大 
        return lowest_common_ancestor(root.right, p, q)
    elif root.val > q.val and root.val > p.val: # p q 的 val 比 root 的 val 都要小, 说明root需要左移减小
        return lowest_common_ancestor(root.left, p, q)
    else:
        return root # 如果 q < root < p 或者 p < root < q, 说明root为 BST的最近祖先(因为BST性质的存在, 因此该root一定为最近祖先)

# dfs - preorder - non recursion
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    while root:
        if root.val < q.val and root.val < p.val:
            root = root.right
        elif root.val > q.val and root.val > p.val:
            root = root.left
        else:
            return root

"""
找到二叉树(BT)的最近公共祖先 leetcode offer 68 ||
该题目相较上一题有一些难度, 原因在于二叉树不能判断粗左右子节点谁的值更大, 所用采用压栈的方式找出, 两种方法:
1. 压栈, 前序遍历, 从root->q 和 从root->p 整个路线上的所有节点, 然后找到两个栈最后端最后一次保持相同的元素, 即为最近公共祖先 
    stack_1 : 6(root) -> 2 -> 4 -> 3(q)
    stack_2 : 6(root) -> 2 -> 4 -> 5(p)

2. 后续遍历, root -> q 和 root-> p 搜索, 到最底层(leaf node), 无非三种情况, node 为空,  node 为 q, node 为 p
    回溯过程: 还是三种情况, 左边node 没有, 右边树没有, 左右边树有


     6    例如: p =  3, q = 5
   /   \
  2     8
 / \   / \
0   4  7  9
   / \ 
   3  5
"""

# stack dfs pre_order

def lowest_common_ancestor_bt(root, q, p):
    if not root:
        return None
    stack_1 = []
    stacK_2 = []
    def pre_order(root, target, stack):
        if not root: # 到底了, 没找到target
            return False
        
        stack.append(target) # root不是空值, 压栈

        if root.val == target.val: # search路上找到了, 返回True
            return True

        left_result = pre_order(root.left, target, stack) # 返回左右结果
        right_result = pre_order(root.right, target, stack)

        if left_result or right_result: # 左右随便一边找到了, 返回true
            return True

        stack.pop() # 左右都没找到, 站定退出
    
    pre_order(root, p, stack_1)
    pre_order(root, q, stack_2)

    # 找相似
    i = 0
    res = None
    while i < len(stack_1) and i < len(stack_2) and stack_1[i] != stack_2[i]:
        res = stack_1[1]
    return res

# dfs pos_order

def lowest_common_ancestor_bt(root, q, p):
    if not root or root == q or root == p: # 3种情况, 到底, 遇到q, 遇到p
        return root
    left_node = lowest_common_anscestor_bt(root.left, q, p)
    right_node = lowest_common_anscestor_bt(root.right, q, p)

    if not left_node:
        return right_node
    if not right_node:
        return left_ndoe
    return root
        
        
