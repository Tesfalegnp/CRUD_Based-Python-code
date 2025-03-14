import os
                # Finctio Area 
def search():
        print("Searching")
def delete():
        if os.path.exists("data.txt"):
                os.remove("data.txt")
        else:
                print("The File is Not existed")
def update():
        print("Updating")
def register():
        print("\tRegister Here")
        global f_name,l_name,age, arr
        file=open("data.txt","a")
        f_name=input("Enter your First name ")
        l_name=input("Enter Last Name ")
        age=input("Enter your Age ")
        arr=[f_name,l_name,age] #To hold Data in Array way
        file.write("\nFirst Name:"+f_name)        
        file.write("\nFirst Last:"+l_name)
        file.write("\nAge :"+age)
        file.write("\n________________________________________\n")
        file.close()
        display() #Calling function
        
def display():
        print("Your Stored Data Are\n")
        file=open("data.txt","r")
        print(file.read())
        file.close()
        if os.path.exists("data.txt"):
                print("file is existed")
        else:
                print("Doesn't existed")
        # print("first Name:"+f_name)
        # print("Last Name:"+l_name)
        # print("Age:"+age)
        
        # cop=list(arr) #Copy From arr to cop
        # for i in cop:
        #         print(i)
                
        
print("Hello  Every one Today i Started Pyhthon Code!\n\n")
print("\tmanu option\n\t 1-register\n\t 2-display\n\t 3-Search\n\t 4-Delete \n\t 5-Uptdate\n\t 6-Check The file")
choice=input("Enter your Choice")
ne_ch=int(choice) #parsing
if ne_ch==1:
        register()
elif 2== ne_ch:
        display()    
elif 3== ne_ch:
        search()
elif 4==ne_ch:
        delete()
elif 5==ne_ch:
        update()
elif 6==ne_ch:
        check()
   
   
   
   
   
   
   
   
   
   
   
            #The Sum of Two Number
# def add(a,b):
#     return a+b 
# n1=int(input("Enter first Number!"))
# n2=int(input("Enter secodse Number!"))
# result=add(n1,n2)
# print("You Entered: ",n1," And: ",n2," Then The Last Result Is:-",result)

# For Loop
# num=['ayyy','bs','ac']
# num=[1j,2j,3e4]
# # num='sume'
# for i in num:
#  n1=i
# print(type(n1))

        #Range
# for i in range(-1,3):
#     print("-",i)
#     print("two")


#         #if check form
# x="how old are you?"
# if "a" in x:
#     print("Yes")
# else:
#     print("Not Are't")

# txt=input("Write Something")
# print("you wrote is:'","'\n\n\n")
 