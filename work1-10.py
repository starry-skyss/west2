import random
l=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#print(l)
l=l+l+l+l
l=l+['king','kinglet']
#print(l)
random.shuffle(l)
#print(l)
l1=l[:17]
l2=l[17:34]
l3=l[34:51]
l4=l[51:]
s=' '
l1=s.join(l1)
l2=s.join(l2)
l3=s.join(l3)
l4=s.join(l4)
#print(l1)
#print(l2)
#print(l3)
#print(l4)

paixu_dict={'kinglet':15,'king':14,'2':13,'A':12,'K':11,'Q':10,'J':9,'10':8,'9':7,'8':6,'7':5,'6':4,'5':3,'4':2,'3':1}
paixu_dict2=dict(zip(paixu_dict.values(),paixu_dict.keys()))
def paixu(list1):
    li=[]
    for i in range(len(list1)):
        card=list1[i]
        num=paixu_dict[card]
        li.append(num)
    li.sort()
    li.reverse()
    list1.clear()
    for i in range(len(li)):
        num=li[i]
        card=paixu_dict2[num]
        list1.append(card)
    return list1
l1=paixu(l1)
l2=paixu(l2)
l3=paixu(l3)
l4=paixu(l4)
print(l1)
print(l2)
print(l3)
print(l4)
w=open('player1.txt','w')
w.write(l1)
w=open('player2.txt','w')
w.write(l2)
w=open('player3.txt','w')
w.write(l3)
w=open('others.txt','w')
w.write(l4)
w.close()
