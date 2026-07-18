import sys

def try_total(back, n, A):
    D = [0] * (n + 1)
    directions = [''] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 1:
            D[i] = A[i] + back
        else:
            D[i] = A[i]
        step = D[i] - D[i - 1]
        if step != 0 and step != 1:
            return None
        directions[i] = '>' if step == 1 else '<'
    if D[n] != back:
        return None
    return ''.join(directions[1:])

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:1+n]))

    g = [0] * (n + 1)

    
    for i in range(1, n+1):
        g[i] = a[i-1] - (n- i)

    # somma alternata
    A = [0] * (n +1)
    for i in range(1, n+1):
        A[i] = g[i] - A[i-1]

    result = None


     # n dispari e due canditati
    if n % 2 == 0:
        result = try_total(A[n], n, A)
    else:
        for candidate in (-A[1], 1 - A[1]):
            result = try_total(candidate, n, A)
            if result is not None:
                break

    if result is None:
        print("impossible")
    else:
        print("possible")
        print(result)

main()