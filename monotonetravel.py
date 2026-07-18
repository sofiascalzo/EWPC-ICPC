import sys
from heapq import heappush, heappop

def solve_direction(n, m, edges_sorted, dist):
   
    INF =float('inf')
    
    i =0
    while i< m:
        
        cur_w = edges_sorted[i][0]
        j=i
        while j<m and edges_sorted[j][0]== cur_w:
            j+=1

        node_block = set()
        adj_local = {}
        for k in range(i,j):
            w, a,b = edges_sorted[k]
            node_block.add(a)
            node_block.add(b)

            if a not in adj_local:
                adj_local[a] =[]

            adj_local[a].append(b)

        local_dist ={}
        heap =[]

        for v in node_block:

            if dist[v] <INF:

                local_dist[v]= dist[v]
                heappush(heap,(dist[v], v))
        



        while heap:
            d, u = heappop(heap)
            if d >local_dist.get(u,INF):
                continue
            if u in adj_local:

                for v in adj_local[u]:

                    nd = d+cur_w

                    if nd < local_dist.get(v,  INF):
                        local_dist[v] =nd
                        heappush(heap, (nd ,  v))
        
        # commit dei nuovi dist
        for v, d in local_dist.items():
            if d <dist[v]:
                dist[v] =d
        
        i = j

def main():
    input = sys.stdin.buffer.read().split()
    pos = 0
    n = int(input[pos])
    
    pos += 1
    m = int(input[pos])
    pos += 1
    
    edges = []
    for _ in range(m):

        a = int(input[pos])
        pos += 1

        b = int(input[pos])
        pos += 1

        w = int(input[pos])
        pos += 1
        edges.append((w, a, b))
    
    INF = float('inf')
    
    
    edges.sort()
    dist_up = [INF] * (n + 1)
    dist_up[1] = 0
    solve_direction(n, m, edges, dist_up )
    

    edges.sort(reverse=True)
    dist_down = [INF] * (n +1)
    dist_down[1] = 0
    solve_direction( n, m,edges, dist_down)
    
    out = min(dist_up[n],dist_down[n] )
    if out>= INF:
        print("impossible")
    else:
        print( out )

main()