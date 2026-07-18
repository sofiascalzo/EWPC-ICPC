import sys 

def main():
    input = sys.stdin.read().split()
    n = int(input[0])

    paintings =[]
    i=1
    for i in range(n):
        my_time = int(input[1+3*i])
        delivery_time = int(input[2+3*i])
        his_time = int(input[3+3*i])

        release_time = my_time + delivery_time 
        paintings.append((release_time, his_time))

    paintings.sort(key=lambda x: x[0])

    release, his_time = paintings[0]
    current_time = release + his_time
        
    for j in range(1,n):
        release, his_time = paintings[j]
        current_time = max(current_time, release) + his_time

    print(current_time)

main()