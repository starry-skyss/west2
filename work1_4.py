a=input('请输入列表，并用空格间隔元素：').split(' ')
print(a)
b=[]
def ispostive(s):
    if s[0]=="-":
        s=s[1:]
#       print(s)
        return s

for i in range(len(a)):
    c=0
    if a[i]=='':
        print('s')
        continue
    if ispostive(a[i]):
        c=1
        a[i]=ispostive(a[i])
#        print(a[i])
    if a[i].isdigit():
        if c==1:
            a[i]=('-'+a[i])
        b.append(int(a[i]))
#print(b)
for j in range(len(b)-1):
    for i in range(len(b)-j-1):
        if b[i]>b[i+1] :
            m=b[i]
            b[i]=b[i+1]
            b[i+1]=m
print(b)
