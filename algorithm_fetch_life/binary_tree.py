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
二叉树展开为链表, leetcode:22
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


