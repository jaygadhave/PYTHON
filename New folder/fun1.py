def add(a1,a2):
	print(a1+a2)
	return a1+a2

def unit_test_add():
  	result=add(2,3)
  	if result!=5:
  		raise exception('Test Failed')

if __name__ =='__main__':
unit_test_add()
