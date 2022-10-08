class bank: #class
    bank_name="Bhikarchot Bank"   #class variable
    def __init__(self,name,addr,age):
       self.naam = name
       self.pata = addr
       self.umar = age
       self.balance = 0
    def check_balance(self): #class method
       print(f'balance of {self.naam} is {self.balance}')
    def deposit(self,amount):
       self.balance = self.balance+amount
    def withdraw(self,amount):
       if self.balance >= amount:
            self.balance = self.balance
       else:
            raise Exception(f'{self.naam} has insufficient fund')

cust1 = bank('karan','moon','007')
cust2 = bank('pawan','mars','008')
cust3 = bank('jay','jupiter','009')

cust1.check_balance()
cust2.check_balance()
cust3.check_balance()
'''
class parent1:
	var1 = "parent class"
	def f1(self):
		print("I am in parent")

class parent2:
	var1 = "1parent class"
	def f1(self):
		print("I am in parent")

class child(parent1,parent1nt2):
	var2 = "child class"
	def f1(self):
		print("I am a child")
	def __str__(self):
		return 'jay'
	def __add__(self,v1):
		return v1

c1 = child()
print(c1.var1)
c1.f1()
c=child()
print(c+5)


import re
phone = "123-456-789 #this is phone number"
num = re.sub(r'#.*$',"",phone)
print(num)
num1=re.sub(r'\D',"",phone)
print(num1)

list1 = [x*x for x in range(5)]
list2 = (x*x for x in range(5))
print(list1)
print(list2)
C
print(next(list2))
print(next(list2))
print(next(list2))
print(next(list2))

def find_even_number_generator(number_stream):
	for n in number_stream:
		if n % 2 == 0:
			yield n

b=find_even_number_generator([1,2,3,4,5,6,7,8,9])
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6]
a=zip(list1,list2)
print(list(a))

keys = ['a','b']
values = [1,2]
d1 = dict(zip(keys,values))
print(d1) 
'''
