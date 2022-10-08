''' list=[]
n=int(input("How many element in list"))
for i in range(0, n):
	#print("Enter number at location", i, ":")
	input=int(input("Enter number at location", i, ":"))
	list.append(input)
print("list"+list)
'''
numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
numberList.reverse()
pos=int(input("Which position highest no find from the list : "))
'''po=pos-1'''
print(numberList[pos])