d = {
    '00001' : 'july',
    '00002' : 'micheal',
    '00003' : 'mary',
    '00004' : 'Junny'
    }
l=[]
for name in d:
    if (int(name[4]))%2==0:
        l.append(name)
for j in range(len(l)):
    del d[l[j]]

for name in d:
   print(d[name])
