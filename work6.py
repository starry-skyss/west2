s = ''
li = ['31415926', '114514', '0123456789']
n = s.join(li)
#print(num)
def sum(num):
    one=two=three=four=five=six=seven=eight=nine=zero=0
    for i in range(len(num)):
        if int(num[i])==1:
            one+=1
        elif int(num[i])==2:
            two+=1
        elif int(num[i])==3:
            three+=1
        elif int(num[i])==4:
            four+=1
        elif int(num[i])==5:
            five+=1
        elif int(num[i])==6:
            six+=1
        elif int(num[i])==7:
            seven+=1
        elif int(num[i])==8:
            eight+=1
        elif int(num[i])==9:
            nine+=1
        else :
            zero+=1
    d={
        '1:':one,
        '2:':two,
        '3:':three,
        '4:':four,
        '5:':five,
        '6:':six,
        '7:':seven,
        '8:':eight,
        '9:':nine,
        '0:':zero
        }
    return d;
dic=sum(n)
for name in dic:
    print(name,dic[name])
