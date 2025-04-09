n,m= map(int,input().split())
a=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]

room=0

for i in range(1,n) :#前綷和
    a[i]+=a[i-1]

total=a[n-1]#最後一項=總和

for qi in q:
    if room>0 :#這是要找的值
        qi+=a[room-1]
    if qi > total:#直接繞一圈
        room=0
        qi-=total
    if a[room]>qi:
        room=(room+1)%n
        continue

    jump=(n-room)//2
    while jump >0:
        while room+jump<n and a[room+jump] < qi:
            room+=jump
            jump//=2
    room=(room+2)%n

    print(room)



