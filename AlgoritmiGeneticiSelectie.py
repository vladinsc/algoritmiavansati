a, b, c = map(int, input().split())
n = int(input())
croms = list(map(float, input().split()))

fitness = [(a*(x**2) + b*x +c ) for x in croms]

F = 0
for f in fitness:
    F += f

p_curent = 0.000000
print(f"{p_curent: .6f}")
for f in fitness:
    prob = f/F
    p_curent += prob
    print(f"{p_curent:.6f}")
