m,n = map(int,input().split())

team_list= [ ]
for _ in range(n):#加入隊伍到team_list
    team_list.append(input())

fullmask=(1<<m) -1

sort_list=[]
for x in team_list:
    team=0
    for ch in x:
        team |=1<< (ord(ch)-ord('A'))
    sort_list.append(team)  

count=0
for i in sort_list:
    for j in sort_list:
        if (i|j)==fullmask and (i&j)==0:
            count+=1
print(count)



