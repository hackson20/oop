

class b:
    def __init__(self,name,roll_no,std,div):
        self.name = name
        self.rollno = roll_no
        self.std = std
        self.div = div
    def printde(self):
        return f"the name is {self.name}\n roll number of {self.name} is {self.rollno}\n {self.name} class is {self.std}\n {self.name} div is {self.div}"
    @classmethod
    def fromdash(cls,string):
        return cls(*string.split("-"))
    @classmethod
    def fromslash(cls,string):
        return cls(*string.split("/"))
    @classmethod
    def fromdot(cls,string):
        return cls(*string.split("."))
    # @staticmethod
    # def print1(parameter_list):
    #     print(parameter_list)



# e = a.fromdash('yogesh-23-8-A')
# e1 = a.fromslash('daksh/6/8/A')
# e2 = a.fromdot('sahil.17.8.A')
# print(e.printde())
# print(e1.printde())
# print(e2.printde())



while 1:
    a = input("enter name:- ")
    a1 = input("enter roll number:- ")
    a2 = input("enter stander:- ")
    a3 = input("enter division:- ")
    o = input("method to make object (-,/,.)")
    if o == '-':
        c = b.fromdash(f"{a}-{a1}-{a2}-{a3}")
        print(c.printde())
    elif o == '.':
        c = b.fromdot(f"{a}.{a1}.{a2}.{a3}")
        print(c.printde())
    elif o == '/':
        c = b.fromslash(f"{a}/{a1}/{a2}/{a3}")
        print(c.printde())
    else:
        c = b(a,a1,a2,a3)
        print(c.printde())

    i = input("do u want to continue (yes,no):- ")
    if i == 'yes' or i == 'Yes' or i == 'y' or i == 'Y' or i == 'YES':
        continue
    elif i == 'no' or i == 'No' or i == 'n' or i == 'N' or i == 'NO':
        break
    else:
        break

quit()