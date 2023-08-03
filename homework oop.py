class cat():
    def __init__(self,name,price,age):
        self.name=name
        self.price=price
        self.age=age
    def getAttribuite(self):
        return self.age ,self.name ,self.price
    def sit(self):
        print("this will be sit when the lunch is done")
    def display(self):
        print(self.age,self.name,self.price)
koke=cat("koke",250,8)
koke.age
print(koke.age)
print(koke.getAttribuite())
koke.name="rex"
print(koke.getAttribuite())
