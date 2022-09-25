for _ in range(int(input())):
    ans=0
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    for x in l2:
        if x in l1:
            l1.remove(x)
        else:
            if x not in l1:
                ans+=1
            ans+=1
    print(ans) 