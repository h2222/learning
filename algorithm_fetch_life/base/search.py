#utf-8
from random import randint, sample, shuffle

class Node:
    def __init__(self):
        self.val = None
        self.next = None

class TreeNode:
    def __init__(self):
        self.val = None
        self.left_node = None
        self.right_node = None


class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def build_default_graph(self):
        """
          0 1 2 3
        0 0 1 1 0 
        1 0 0 1 0
        2 1 0 0 1
        3 0 0 0 1
        """
        self.add_edge(0, 1) 
        self.add_edge(0, 2) 
        self.add_edge(1, 2) 
        self.add_edge(2, 0) 
        self.add_edge(2, 3) 
        self.add_edge(3, 3)
        print("graph print: ", self.graph)



"""
二分查找:
已排序数列
时间复杂度: O(logn)
"""
def binary_search(ls):
    target = sample(ls, 1)[0]
    print("orginal:", ls)
    ls.sort()
    print("target:", target)
    def sub_search(ls):
        h = 0
        t = len(ls)
        while h <= t:
            mid = h + (t - h) // 2
            if ls[mid] == target:
                return mid
            elif ls[mid] < target:
                h = mid + 1
            elif ls[mid] > target:
                t = mid - 1
        return "no found"
    print("target idx:", sub_search(ls))
    shuffle(ls)


"""
扭转二分查找
"""


def twist_binary_search(ls):
    target = sample(ls, 1)[0]
    ls.sort()
    ls = ls[4:] + ls[:4]
    print("orginal:", ls)
    print("target:", target)
    def sub_search(ls):
        h = 0
        t = len(ls) - 1
        while h <= t:
            mid = (h + t) // 2
            if ls[mid] == target:
                return mid
            elif ls[0] <= ls[mid]:  # 说明 顺序正常 mid 顺序扭转
                if ls[0] <= target < ls[mid]:
                    t = mid - 1# target 落在前半部分, t向前收紧
                else:
                    h = mid + 1# target 落在后半部分, h向后收紧
            else:                   # 说明  顺序扭转 mid 顺序正常
                if ls[mid] < target <= ls[len(ls) - 1]:
                    h = mid + 1
                else:
                    t = mid - 1
        return "not found"
    print("target idx:", sub_search(ls))
    shuffle(ls)




def DFS():
    g = Graph()
    g.build_default_graph()
    start_point = 0

    def forward(g, visited, start_point):
        visited[start_point] = True
        print(visited)
        print(start_point)
        for i in g.graph[start_point]: # 定点分叉搜索
            if visited[i] == False: # 访问过的就不访问了
                forward(g, visited, i)

    def dfs_search(g, start_point):
        visited = [False] * (max(g.graph)+1)
        print(visited)
        forward(g, visited, start_point)

    dfs_search(g, start_point)



def BFS():
    g = Graph()
    g.build_default_graph()
    start = 0
    def search(g, start):
        queue = []
        visited = [False] * len(g.graph)
        visited[start] = True
        queue.append(start)
        while queue:
            start = queue.pop(0) # 抛去头部
            print(start, end=' ')
            for i in g.graph[start]:  # 循环遍历start的临近点
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True     # 设置访问 
    search(g, start)

def a_star():
    pass





if __name__ == "__main__":
    ls = [randint(-100, 100) for _ in range(20)]
    binary_search(ls)
    twist_binary_search(ls)
    DFS()
    BFS()