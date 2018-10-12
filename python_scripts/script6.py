class temp:
    var1=0

    def __init__(self,var2,var3):
        self.var2 = var2
        self.var3 = var3
        temp.var1 = self.var1+1

    def add(self):
        try:
            self.sum = self.var3 + self.var4
        except Exception:
            self.sum = self.var2 + self.var3


t1 = temp(3,4)

print(t1.var1, t1.var2, t1.var3)

t1.var4 = 8
t1.add()
print(t1.var1, t1.var2, t1.var3, t1.sum)

t2 = temp(5,10)

print(t2.var1, t2.var2, t2.var3)
t2.add()
t2.val = 8
print(t2.var1, t2.var2, t2.var3, t2.sum)
