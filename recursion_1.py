a=list(input().split())
i=-1

def main():
    global i
    i+=1
    print(i)
    if a[i]=="f":
        x=main()
        
        return x*2-3
    elif a[i]=="g":
        x=main()
        y=main()
        
        return 2*x+y-7
    elif a[i]=="h":
        x=main()
        y=main()
        z=main()
       
        return 3*x-2*y+z
    else:
        return int(a[i])
    
print(main())