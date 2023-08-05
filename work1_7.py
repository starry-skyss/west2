class Commodity:
    def __init__(self,num,name,price,amo,reamo):
        self.num=num
        self.name=name
        self.price=price
        self.amo=amo
        self.reamo=reamo

    def display(self):
        print('%s,%s,%.2f,%d,%d' %(self.num,self.name,self.price,self.amo,self.reamo))

    def income(self):
        return self.price*(self.amo-self.reamo)

    def setdata_num(self,num):
        self.num=num
    def setdata_name(self,name):
        self.name=name
    def setdata_price(self,price):
        self.price=price
    def setdata_amo(self,amo):    
        self.amo=amo
    def setdata_reamo(self,reamo):
        self.reamo=reamo
apple=Commodity('001','apple',1.55,100,35)
money=apple.income()
print('The value of the goods sold is %.2f' %money)
apple.display()
apple.setdata_reamo(17)
apple.display()
money=apple.income()
print('The value of the goods sold is %.2f' %money)
