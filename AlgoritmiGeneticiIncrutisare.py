l = int(input())
c1 = input()
c2 = input()
i = int(input())

c1_nou = c1[:i] +c2[i:]
c2_nou = c2[:i] + c1[i:]
print(c1_nou)
print(c2_nou)