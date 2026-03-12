t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    distinct_colors = len(set(arr))
    
    
    print(distinct_colors)