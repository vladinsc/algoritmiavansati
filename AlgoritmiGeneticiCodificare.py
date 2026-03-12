a, b= map(float, input().split())
p = int(input()) #precizie
m = int(input()) # nr de teste
print(p)
import math

l = math.ceil(math.log((b-a) * (10**p), 2)) # numar biti codificare
d = (b-a)/(2**l)

def encode(number: float) -> str:
    ratio = (number - a) / (b - a)
    k = math.floor(ratio * (2 ** l))
    bin_str = bin(k)[2:].zfill(l) # string de biti 0 adaugati
    return bin_str

def decode(bin_str: str) -> float:
    k = int(bin_str,2)
    return a + k*d



for _ in range(m):
    tip_op = input()
    if tip_op == 'TO':
        x = float(input())
        print(encode(x))
    elif tip_op == 'FROM':
        bin_str = input().strip()
        print(f"{decode(bin_str): .{p+3}f}")


