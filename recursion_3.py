string = input()   
n = int(input())             
cntt = 0
inx = -1                     

def cnt(size):
    global cntt, inx

    inx += 1
    if inx >= len(string):
        return

    if string[inx] == '2':
        size = size // 2
        cnt(size)
        cnt(size)
        cnt(size)
        cnt(size)

    elif string[inx] == '1':
        cntt += size * size
        return   

    elif string[inx] == '0':
        return   

cnt(n)
print(cntt)
