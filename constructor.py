class shopping:
    def __init__(self,place):
        self.place=place
        print("welcome to shopping at",place)    
    def dresstype(self,dt):
        self.d=dt
    def price(self,pr):
        self.p=pr
    def size(self,sz):
        self.s=sz
    def display(self):
        print(self.d)
        print(self.p)
        print(self.s)
        print(self.place)
k = shopping("zudio")
k.dresstype("kurti")
k.price(500)
k.size(40)
k.display()