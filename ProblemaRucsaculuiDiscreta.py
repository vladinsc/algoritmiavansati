n, c  = map(int, input().split())
val = list(map(int, input().split()))
weight = list(map(int, input().split()))

def knapsacrec(C, n, val, weight, dp):
    if n == 0 or C == 0:
        return 0
    if dp[n][C] != -1: return dp[n][C]

    pick = 0

    if weight[n-1] <= C:
        pick = val[n-1] + knapsacrec(C-weight[n-1], n-1, val, weight, dp)
    notPick = knapsacrec(C, n-1, val, weight, dp)

    dp[n][C] = max(pick, notPick)

    return dp[n][C]
dp = [[-1]*(c+1) for _ in range(n+1)]

print (knapsacrec(c, n, val, weight, dp))

