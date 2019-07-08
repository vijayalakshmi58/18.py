# 18.py
t,s=map(int,input().split())
for m in range(t+1,s):
    sum=0
    num=m
    while num>0:
        dig=num%10
        sum+=dig**3
        num//=10
        if(m==sum):
            print(m,end=" ")
