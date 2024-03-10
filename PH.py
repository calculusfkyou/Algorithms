while 1:
    try:
        n=int(input())
        grid=list(map(int,input().split()))
        ans=[0]*n
        ans[0]=grid[0]
        ans[1]=grid[1]
        for i in range(2,n):
            t=min(ans[i-2],ans[i-1])
            ans[i]=grid[i]+t
        print(ans[len(ans)-1])
    except EOFError:
        break