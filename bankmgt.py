data={}
list1=["Name","Address","Phone","Govt ID","Account Type","Amount"]

def take_data():
    acc_num=input("enter account no:")
   
    for item in list1:
        list2.append(input("Enter %s:"%item))
       
    data[acc_num]= dict(zip(list1,list2))
    print("Account created")
    print("*"*20)
    return
     
while true:
    list2=[]
    ch=int(input("1.New customer\n2.Existing customer\n3.Exit\nEnter Choice:"))
       