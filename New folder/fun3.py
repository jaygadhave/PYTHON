def add(n1,n2):
  return n1+n2
a=add(5,1)
b=add
c=b(2,3)
print(a)
print(c)


def parent():
	def child():
		print('I am child')
	return child
b=parent()
b()	


def decor(f):
 def wrap():
 	print('executing function')
 	f()
 	print('done')
 return wrap
def greet():
	print('hi')
a=decor(greet)
a()
greet=decor(greet)
greet()
