class ai:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

students=ai("Ramesh",30,"A.P.")

print(f'{students.name},{students.age},{students.address}')


# class bike:

#     def __init__(self,name,model,launched):
#         self.name=name
#         self.model=model
#         self.launched=launched

# mod1=bike("Duke ktm 250",250,"mar2025")
# mod2=bike("KTM 390 Adventure R",390,"jan2025")
# mod3=bike("KTM 125 Duke",125,"feb2025")
# mod4=bike("KTM390 SMC R","390SMC","mar2025")
# print(f'{mod1.name},{mod1.model},{mod1.launched}')
# print(f'{mod2.name},{mod2.model},{mod2.launched}')
# print(f'{mod3.name},{mod3.model},{mod3.launched}')
# print(f'{mod4.name},{mod4.model},{mod4.launched}')

        

# class car:
#     a="vehicle"
#     b="car"

#     def abc(self):
#         print("Hello :",self.a)
#         print("Hello :",self.b)

#     def xyz(self):
#         print("All the vehicles.")

# x=car()

# print(f'{x.a},{x.b}')
# print(x.a)
# print(x.b)
# x.abc()
# x.xyz()




# class math:
#     a=9
#     b=10

#     def add(self):
#         x=self.a+self.b
#         print("Add",x)

#     def sub(self):
#         y=self.a-self.b
#         print("SUB",y)

#     def mul(self):
#         a=self.a*self.b
#         print("mul",a)

#     def div(self):
#         p=self.a/self.b
#         print("div",p)

# z=math()
# z.add()
# z.sub()
# z.mul()
# z.div()


# class wallet:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance


#     def add_money(self,money=0):
#         if money>0:
#             self.balance +=money
#             print(f'money added:{money} to {self.balance}')
#         else:
#             print("Enter a valid amonut.")
    
#     def spend_money(self,money):
#         if money > self.balance:
#             print("Insufficient balance.")
#         else:
#             original_balance=self.balance
#             self.balance-=money
#             print(f'spend Amount {money} from {original_balance} remaining balance :{self.balance}')

#     def check(self):
#         print(f'{self.name} balance is {self.balance}')

# x=wallet("Ankit",100)
# y=wallet("Anuj",500)

# x.add_money(500)
# x.add_money(50)

# x.spend_money(99)
# y.spend_money(49)

# x.check()
# y.check()

# class Flipkart:
#     def __init__(self,name):
#         self.name=name
#         self.item=[]

#     def add_item(self,i_name,price):
#         self.item.append({'name':i_name,'price':price})
#         print(f'Added {i_name} to list with price {price}')

#     def remove(self,i_name):
#         for item in self.item:
#             if item['name']==i_name:
#                 self.item.remove(item)
#                 print(f'Removed {i_name}')
#                 return
#         print(f'{i_name} not found')

#     def display_c(self):
#         if self.item:
#             print(f'cart for {self.name}')
#             for item in self.item:
#                 print(f' {item['name']} : {item['price']}')

#         else:
#             print("Cart is empty:")

# x=Flipkart("Ankit")
# x.add_item("Laptop", 50000)

# x.display_c()
