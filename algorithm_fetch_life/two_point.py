from random import randint




"""
最小替换步数 leetcode 1347
s = "bab"
t = "aba"
t 替换为 "abb" 1个a, 2个b, 与 s相同
"""

def min_step(s, t):
    # 双指针
    # 先排序随后使用双指针对相同字符进行配对。
    # 答案为字符串长度减去配对数。
    # ['a', 'a', 'a', 'b', 'b', 'b'] i
    # ['a', 'a', 'b', 'b', 'b', 'w'] j
    s = sorted(s)
    t = sorted(t)
    i = 0
    j = 0
    same_num = 0
    length = len(s)

    while i < length and j < length:
        if s[i] == t[j]:
            i += 1
            j += 1
            same_num += 1
        elif s[i] > t[j]:
            j += 1
        else:
            i += 1
        if i == length or j == length:
            break
    res  = length - same_num
    print(res)
    return res

if __name__ == "__main__":
    min_step("ababba", "bababw")