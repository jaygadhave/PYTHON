a=10
b=15
print(a==b)

print('\n')

print('abc'>'abd')
'a'=='A'
print(ord('a'))
print(ord('A'))
print('A'<'a')

print('\n')

a=[1,2,3,4,5,6]
print(5 in a)
print(8 in a)
print(5 not in a)
print(9 not in a)

print('\n')

str='My name is jay'
print('jay' in str)
print('name' in str)
print(' ' in str)

print('\n')

a=100
b=100
print(a is b)
a=[1,2,3,4,5,6,7,8,9]
b=[0,1,2,3,4,5,6,7,8]
print(a is b)
a=[1]
b=[1]
print(a is b)
a=b
print(a is b)
print(id(a))
print(id(b))

print('\n')

name='jay'
name1='jay'
if name == name1:
  print ('Name is same')
else:
  print ('Name is not same')
  
print('\n')

'''
result=int(input('enter percentage:'))
if result>=80:
   print("you got first division")
   print("your rank is 2nd")
elif result<80 and result>60:
   print("you got Second division")
   print("your rank is 3rd")
elif result<60 and result>40:
   print("you got third division")
   print("your rank is above 10")
elif result<40 and result>33:
   print("you got third division")
   print("your rank is above 15")
else:
   print('Error')
print('Thank you')
'''

print('\n')
'''
dic={1:{'name':'jay','fname':'digambar','english':56,'maths':67,'science':45},
     2:{'name':'akshay','fname':'vitthal','english':65,'maths':68,'science':54}}
rollno=int(input('enter rollno:'))
if rollno in dic:
   print('-'*20)
   print('name:',dic[rollno]['name'])
   print('Father name:',dic[rollno]['fname'])
   print('-'*20)
   print('english:',dic[rollno]['english'])
   print('maths:',dic[rollno]['maths'])
   print('science:',dic[rollno]['science'])
   print('-'*20)
   total=print('percentage:',(dic[rollno]['english']+dic[rollno]['maths']+dic[rollno]['science'])/3)
else:
   print('error')
'''
name=(input('enter name:'))
fname=(input('enter father name'))
english=int(input('enter marks of english:'))
maths=int(input('enter marks of maths:'))
science=int(input('enter marks of science:'))
dic={1:{},
     2:{}}

print('-'*20)
print('name:',name)
print('Father name:',dic[1][''])
print('-'*20)
print('english:',dic[1][''])
print('maths:',dic[1][''])
print('science:',dic[1][''])
print('-'*20)
total=print('percentage:',(dic[1]['']+dic[1]['']+dic[1][''])/3)








   
   
 
   

   

























  

  




























