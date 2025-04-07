n,l=map(int,input().split())
a=[0]+[int(x)for x in input().split()]+[l]
cnt=0

def cut(start,end):
    global cnt
    mid=(a[start]+a[end])//2
    i=0
    if end-start<=1:
        return 0
    cnt+=a[end]-a[start]
    while a[i] < mid:
        i+=1
    if a[mid]-a[i-1] <= a[i]-a[mid]:
        i=i-1
    cut(start,i)
    cut(i,end)   
    return(cnt)

print(cut(0,n+1))
