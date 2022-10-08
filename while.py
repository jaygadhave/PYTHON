i=1
while i<3:
  print('The number is %d'%i)
  i+=1
  
print('\n')

numbers=[1,2,3,4,5,6,7,8]
for num in numbers:
  print (num,end=' ')
  
print('\n')
'''
a=int(input('enter table no:'))
b=int(input('enter multiple:'))
c=int(input('enter end:'))
i=0
while i<=c:
   print(f"{a} x {i}= {i*a}")
   i+=b
'''
'''
while True:
  no=input("enter the table no: ")
  mul=input("Enter multiples: ")
  end=input("enter end: ")
  if all((no,mul,end)):
    no,mul,end=int(no),int(mul),int(end)
    for i in range(end+1):
      if i%mul !=0:
        continue
      print(f"{no} x {i}={no*i}")
    break
  else:
    print("Please enter values for all question")'''
    
print('\n')

a='='*30                              
b=' '*10
print(a)
print(b,'Menu',b)
print(a)
def menucard():
  print('')




