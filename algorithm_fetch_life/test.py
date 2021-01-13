       
def test(s):
    length = len(s)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        dp[i][i] = 1 # 对角线

    for i in range(length - 2, -1, -1): # 从倒数第二次开始
        start = i + 1
        for j in range(start, length):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2 # 左下 + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # 下边, 左边

    print("?>>>>>")
    return dp[0][length - 1]


if __name__ == "__main__":
    print(test("abc"))
