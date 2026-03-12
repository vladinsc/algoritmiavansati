n, c  = map(int, input().split())
val = list(map(int, input().split()))
weight = list(map(int, input().split()))
obj = [(val[i], weight[i]) for i in range(n)]

obj.sort(key=lambda x: x[0]/x[1], reverse=True)

C = c
valoareMaxima = 0.00
for i in range(n):
    if obj[i][1] <= C:
        valoareMaxima += obj[i][0]
        C -= obj[i][1]
    else:
        valoareMaxima += (obj[i][0]/ obj[i][1]) * C
        break

print(valoareMaxima)
