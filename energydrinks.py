import sys
import math

def main():
    input = sys.stdin.read().split()
    n= int(input[0])
    x=int(input[1])
    c=list(map(int, input[2:2+n]))

    total = math.log2((c[0]+x)/x)
    for i in range(1,n):
        total += math.log2((c[i]+x)/x)

    correction = math.log2((max(c)+x)/max(c))
    total -= correction

    print(f"{total:.10f}")


main()