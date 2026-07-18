import sys 


def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    k=int(input[1])
    price = list(map(int, input[2:2+n]))

    
    best = price[k] - price[0]
    for i in range(n-k):
        earn = price[i+k] - price[i]
        if earn > best:
            best = earn
            
    print(best)
    
main()