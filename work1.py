a=int(input())
b=int(input())
c=int(input())
if a>b:
    if c>a:
        print('%d %d %d' %(c,a,b))
    elif b>c:
        print('%d %d %d' %(a,b,c))
    else :
        print('%d %d %d' %(a,c,b))
else :
    if c>b:
        print('%d %d %d' %(c,b,a))
    elif a>c:
        print('%d %d %d' %(b,a,c))
    else :
        print('%d %d %d' %(b,c,a))
l=[a,b,c]
for j in range(len(l)-1):
    for i in range(len(l)-j-1):
        if l[i]<l[i+1] :
            m=l[i]
            l[i]=l[i+1]
            l[i+1]=m
print('%d %d %d' %(l[0],l[1],l[2]))
