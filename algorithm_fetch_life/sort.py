#utf-8
from random import randint, shuffle
from sys import maxsize
"""
实现各种基础排序
"""


"""
冒泡
time complixity: O(n^2)
"""

def bubble(ls): 
    length = len(ls)
    for i in range(length):
        for j in range(length - i - 1):
            if ls[j] < ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    print(ls)
    shuffle(ls)


"""
选择
time complxity: O(n^2)
"""

def select_sort(ls):
    length = len(ls)
    for i in range(length):
        best_idx = i
        for j in range(i + 1, length):
            if ls[j] > ls[best_idx]:
                best_idx = j
        ls[i], ls[best_idx] = ls[best_idx], ls[i]
    print(ls)
    shuffle(ls)


"""
插入排序
time complxity: O(n^2)
"""
def insert_sort(ls):
    length = len(ls)
    for i in range(1, length):
        target = ls[i]
        j = i - 1
        while j >= 0 and ls[j] < target: # j 向前遍历, 从i-1挨个与target比较
            ls[j + 1] = ls[j] # ls[j] 向后抛到j+1位置
            j -= 1
        ls[j + 1] = target
    print("insert:", ls)
    shuffle(ls)


"""
归并排序
time complexity: O(n*logn), 由递推公式
If the running time of merge sort for a list of length n is T(n)
then the recurrence T(n) = 2T(n/2) + n follows from the definition of the algorithm

一个长度为n的list遍历时间为T(n),   把list劈成2个长度他相同(为原来n的一半)的sub_list, 所需要的运行时间为 2T(n/2)
然后在花费 n 步将2个 sub_list和在一起,  所用最后时间耗时就是 T(n) = 2T(n/2)+n

时间 -> 时间复杂度推导(数学演绎法):
T(n)   =2T(n/2)+n
       =2(2T(n/2*2)+n)+n
       =2(2(2T(n/2*2*2)+n)+n)+n
       =2^3T(n/2^3)+3n
       =...
       =2^kT(n/2^k)+kn    现在设T(1)=0, n=2^k
       =nT(1)+kn
       =kn
       =nlogn
"""

def merge_sort(ls):
    def sub_func(ls):
        if len(ls) > 1: # 出递归条件, sub list中至少得有两个
            mid = len(ls) // 2
            l_part = ls[:mid]
            r_part = ls[mid:]
            # 后续遍历
            sub_func(l_part)
            sub_func(r_part)
            # 第一次到达这里, 说明 ls应该有2个元素, 因为递归条件len(arr) > 1的原因, 你不得不停止递归
            mean_idx = 0
            l_idx = 0
            r_idx = 0
            # 交叉写入ls
            while l_idx < len(l_part) and r_idx < len(r_part):
                if l_part[l_idx] > r_part[r_idx]:
                    ls[mean_idx] = l_part[l_idx]
                    l_idx += 1 # 左part指针向前挪
                else:
                    ls[mean_idx] = r_part[r_idx]
                    r_idx += 1 # 右part指针向前挪
                mean_idx += 1
            # 左右有多余的, 继续添加
            while l_idx < len(l_part):
                ls[mean_idx] = l_part[l_idx]
                l_idx += 1
                mean_idx += 1
            while r_idx < len(r_part):
                ls[mean_idx] = r_part[r_idx]
                r_idx += 1
                mean_idx += 1
    sub_func(ls)
    print("merge:", ls)
    shuffle(ls)


"""
快速排序:
time complexity: O(nlogn)
"""

def quick_sort(ls):
    def sub_func(ls, head, tail):
        if head < tail:
            start = head
            end = tail
            base = ls[head]
            while start < end: # 重合就停止
                while start < end and ls[end] <= base: # 后部分小于base无所谓, 大于在往前换
                    end -= 1
                ls[start] = ls[end] # tail 前挪
                while start < end and ls[start] >= base: # 前面的大于base无所谓, 小于才往前换
                    start += 1
                ls[end] = ls[start] # head 后挪
            ls[start] = base
            sub_func(ls, head, start - 1)
            sub_func(ls, start + 1, tail)
    h = 0
    t = len(ls) - 1
    sub_func(ls, h, t)
    print("quick:", ls)
    shuffle(ls)



"""
堆排序
heap sort (max heap, min heap)
二叉堆是一个完全二叉树, 规则: root node 的value必须小于/大于child node, 前者为max-heap, 后者为min-heap

build heap: 按照数组从左到右依次插入树种
heapify: 保证max/min value root
"""

def heap_sort(ls):
    def heapify(ls, length, i):
        target = i
        l = 2 * i + 1 # left child index
        r = 2 * i + 2 # right child index

        if l < length and ls[l] < ls[target]:
            target = l
        if r < length and ls[r] < ls[target]:
            target = r

        if target != i:
            ls[i], ls[target] = ls[target], ls[i]
            heapify(ls, length, target)

    def sort(ls):
        length = len(ls)
        # build heap
        # 取index的中间值-1, 并逐渐减小, 起始位length//2-1的原因是 2 * (length//2 - 1) = length - 2, 正好为后面还有1个元素, 可以作为child node
        for i in range(length//2-1, -1, -1):
            heapify(ls, length, i)
       
        # transfer head and tail
        for i in range(length - 1, -1, -1):
            ls[i], ls[0] = ls[0], ls[i] # tail to head, head to tail
            heapify(ls, i, 0) # 从最顶部开始heaplify
    sort(ls)
    print(ls)
    shuffle(ls)


"""
计数排序, (非比较排序算法, 核心在于将数值和数值的出现次数转化为键值对, 然后依次写入排序中)
time complexity: O(n+k) n 为元素的类型个数, k为最大值元素的个数, 例如 1 1 1 2 2 3 3 3 3 , n=3, k=4
"""

def count_sort(ls):
    def sub_sort(ls):
        d = {}
        res = []
        min_value = maxsize
        max_value = - maxsize
        for i in ls:
            if i not in d:
                d[i] = 0
            d[i] += 1
            max_value = max(max_value, i) # 找最大边界
            min_value = min(min_value, i) # 找最小边界
        for i in range(max_value, min_value-1, -1): # descent
            if i not in d:
                continue
            for _ in range(d[i]):
                res.append(i)
        return res
    
    res = sub_sort(ls)
    print(res)
    shuffle(ls)


"""
堆排序的应用, 查找一个数组总第k大的数值 nc 88
nums = [1, 3, 5, 2, 2], k = 3
当k = 3, nums中第三大的数值是2
1. 排序, 2.查找   
两种方案: 1.max heap 加查找  2. quick_sort + binary search
"""

# 方案1. max heap + 查找
def find_kth(nums, k = 3):
    print("nums:", sorted(nums))
    def heapify(nums, length, i):
        l = 2 * i  + 1
        r = 2 * i + 2
        target = i
        if l < length and nums[l] < nums[target]:
            target =  l
        if r < length and nums[r] < nums[target]:
            target = r
        if target != i:
            nums[target], nums[i] = nums[i], nums[target]
            heapify(nums, length, target)

        pass
    def find(nums, k):
        length = len(nums)
        for i in range(length//2 -1 , -1, -1):
            heapify(nums, length, i)    
        j = length - 1
        while j >= length - k:   # 正常情况下, 我们使用0进行排序, 但是因为我们需要找到第k大的值, 所用j需要减少到 n - k
            nums[j], nums[0] = nums[0], nums[j]
            heapify(nums, j, 0)
            j -= 1
        return nums[length - k]
    print("the kth value of nums is ", find(nums, k))
    shuffle(nums)





if __name__ == "__main__":
    ls = [randint(-100, 100) for _ in range(20)]
    print("orginal:", ls)
    bubble(ls)
    select_sort(ls)
    insert_sort(ls)
    merge_sort(ls)
    quick_sort(ls)
    heap_sort(ls)
    count_sort(ls)

    #############
    find_kth(ls)