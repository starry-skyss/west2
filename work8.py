import random
l=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
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
w=open('player1.txt','w')
w.write(l1)
w=open('player2.txt','w')
w.write(l2)
w=open('player3.txt','w')
w.write(l3)
w=open('others.txt','w')
w.write(l4)
w.close()
