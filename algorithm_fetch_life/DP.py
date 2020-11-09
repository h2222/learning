# coding=utf-8


'''
动态规划
https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie

动态规划三要素
1. base case
2. 


'''
def fib(n):

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    https://leetcode-cn.com/problems/longest-increasing-subsequence/

    1. base case and initialization: dp 数组, 用于保存当前子序列最大递增长度
    2. 状态: 当前子序列下的最后一个值i 为止, 的上升长度dp[i]
    3. 条件: 如果子序列 前面的 第 j 个值大于 最后一个值 i, 说明j不满足递增序列的要求, 则继续保持dp[i], 即 dp[i] = dp[i]
    """
    dp = [1 for _ in range(len(nums))]
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(dp)
    res = 0    
    for i in dp:
        res = max(res, i)
    
    return res


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # 存储已经遍历的树, 防止超时
    memo = {}
    def coin(n):
        # 1. BASE CASE: 一开始 设零钱为 n, 起始步数为 +inf, 因为要求最小值, 起始步数为最大值,  n=0, n=-1
        # 2. 状态: 自下而上,  n 逐一被 coin 减去, 直到 0 或 -1 为止
        # 3. 状态转移, 每一个减 n,  都有三个选着 即 coins = [1, 2, 5]
        # 4. 状态转移方程:
        # coin(n) = 0  if n = 0
        # coin(n) = -1 if n < 0
        # coin(n) = min(coin(n-coin)+1)  where coin belong to coins
        
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        result = float('inf')
        # 状态转移
        for c in coins:
            sub_problem = coin(n - c)
            # 如果到最底下, 发下这样凑不齐钱, 果断放弃
            if sub_problem == -1:
                continue
            res = min(result, sub_problem+1)
            memo[n] = res if res !=  float('inf') else -1
        return memo[n]
    return coin(amount)




def maxSubArray(nums):
    """
    :type nums: List[int]   
    :rtype: int
    
    0. 初始化: dp 为 以 nums[i] 为结尾的, 前 i 个 子序列的和 
    1. base case: nums[0] 作为 base case, 因为求最大值, 所以从小到大
    2. 状态: 前nums[i]项的最大值组合的和, 最大值组合条件有转移条件判断得到
    3. 转移/条件: max(nums[i], nums[i]+dp[i-1])   nums[i] 表示另外起一个新的子问题(子序列), nums[i]+dp[i-1] 表示在原有基础上继续增长,
        增加和就行
    4. 状态转移方程: dp[i] = nums[i],          num[i] >= dp[i-1]  
                    dp[i] = nums[i]+dp[i-1] , num[i] >= dp[i-1]
    
    5. 特殊情况处理:  nums = []
    """

    if nums == []:
        return 0
    
    dp = [-float('inf') for _ in range(len(nums))]

    dp[0] = nums[0]

    for i in range(1, len(dp)):
        dp[i] = max(nums[i], nums[i]+dp[i-1])

    print(dp)
    res = -float('inf')

    for i in dp:
        res = max(res, i)
    return res 




# DP 01: 背包问题
# https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/bei-bao-wen-ti
def dp_package(N=3, W=4, Wt=[2, 1, 3], Vt=[4, 2, 3]):
    '''
    0. 初始化, 因为背包问题, 有两个状态限制, 即重量和价值, 所以 dp初始化为2维数组 dp[状态1][状态2]为当前状态下物品的价值
    1. base case: 当商品为0时, 所有价值为0
    2. 状态:   重量: 指背包的不同大小的重量W=4,  物品件数: 背包可以装不同数量的物品件数 N=3
    4. 转移条件:   如果当前装的下,  叠加物品价值,   如果装不下或装下了没有,  继续保持前一个物品的价值
    5. 状态转移方程:

        dp[i][w] = dp[i-1][w]  if d[i-1][w] > dp[i-1][W - Wt[i-1]] + Vt[i - 1]
        dp[i][w] = dp[i-1][w]  if W -Wt[i-1] <0
        dp[i][w] = dp[i-1][W-Wt[i-1]] + Vt[i-1]   if <
    '''

    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]  # +1 是为了可以从 1 开始

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j-Wt[i-1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max( dp[i-1][j], 
                                dp[i-1][j-Wt[i-1]]+Vt[i-1]
                              )
    
    return dp[N][W]





def distance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 0:
                dp[0][j] = j  # word1为空字符串, word1只需要添加 j 次就可以变为 word2
                continue
            if j == 0:
                dp[i][0] = i # word2 为空字符串, word1需要删除 i 次变为 word2
                continue
                
            else:
                dp[i][j] = min(dp[i-1][j], dp[j-1][i])+1   # 找到添加1 或删除1那个更小, 但操作都得+1

                # 不用修改, 直接找最小
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j])
                
                # 替换操作, 
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j])
    
    return dp[i][j]




def throw_egg(K, N):

    memo = {}
    def dp(k, n):
        if k == 0:
            return n
        if n == 0:
            return 0
        
        if (k, n) in memo:
            return memo[(k, n)]
        
        res = float('inf')

        for i in range(1, n+1):
            res = min(res, 
                      max(
                          dp(k, n-i),
                          dp(k-1, i-1)
                      )+1
                    )
            memo[(k, n)] = res
            return memo[(k, n)]

    return dp(K, N)


print(dp_package())
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(coinChange([1,2,5], 11))
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
# print(fib(46))