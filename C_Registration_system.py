d={}
for _ in range(int(input())):
    s=input()
    if s not in d:
        d[s]=0
        print("OK")
    else:
        d[s]+=1
        s=s+str(d[s])
        d[s]=0
        print(s)