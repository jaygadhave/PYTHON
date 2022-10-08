var = 'GOODDAYTODAY'
print(var[::-1])

print('\n')

n1 = 'My '
n2 = 'Name '
n3 = 'is '
n4 = 'Jay '
n5 = 'Gadhave'
name = n1+n2+n3+n4+n5
print(name)

print('\n')

name,age,subject,place = 'Jay',21,'Python','Baner'
print("My Name is {0}.I am turning {1} today.".format(name,age))
print("I am studing {} at {a}".format(subject,a=place))

print('\n')

print(f'My Name is {name}.I am turning {age} today.')
print(f"I am studing {subject} at {place}")

print('\n')

name="      HELLO"
a = name.strip()
print(a)

print('\n')

name='jay'
v=len(name)
print(v)

print('\n')

name='JAY'
v=name.lower()
print(v)

print('\n')

name='jay'
v=name.upper()
print(v)

print('\n')

greet = 'Welcome to Ethans Kharadi today'
b=greet.replace('Welcome to ','').replace('Kharadi','baner').upper()
print(b)

print('\n')

greet = 'Welcome to Ethans Kharadi today'
b=greet.split(' ')
print(b)

greet = 'Welcome to Ethans Kharadi today'
b=greet.split('a')
print(b)

print('\n')

'''name = input('Enter your name: ')
print(name)'''

print('\n')

jay_list = ["laptop","mobile","headphones"]
print(jay_list)
jay_list[0]='car'
print(jay_list)
print(type(jay_list))
print(jay_list[1:2])
jay_list.append("laptop")
print(jay_list)
jay_list.remove('car')
print(jay_list)

print('\n')

l1=[1,2,3]
l2=[5,10,11]
l1.append(l2)
l1.extend(l2)
l1.extend('jay')
print(l1)

print('\n')

l6=[1,2,3,[4,5,6,[7,8],3]]
l7=[2,3,4,5,6,7,8,2]
'''print(l6[3][3][1])
print(len(l7))
print(l7.index(2))
print(l7.count(2))
print(l7.index(2,1)'''
l7.insert(3,56)
l7.pop(3)
print(l7)
l7.reverse()
print(l7)
l7.sort()
print(l7)












