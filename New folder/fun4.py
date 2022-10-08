def decor(f):
 def wrapper():
 	print('executing function')
 	f()
 	print('done')
 return wrapper
@decor
def greet():
	print('hi pratiksha')
greet()

def square(n):
	return n*n
a=[1,2,3,4]
b=[1,4,9,16]
c=list(map(square,b))
d=list(map(square,a))
print(c,d) 

def check_greater(n):
	if n>5:
		return True
	else:
		return False

a=[6,7,5,1,9,10]
g=list(filter(check_greater,a))
print(g)

y=list(map(int,input("Enter the 3 no:").split(",")))
print(y)