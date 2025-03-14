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
def check():
        if os.path.exists("data.txt"):
                print("file is existed")
        else:
                print("Doesn't existed")
        # print("first Name:"+f_name)
     
     
      
print("Hello  Every one Don't worries About, Today we Starte Pyhthon Code In Simple Way!\n\n")
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
   
   
   
   
   
   
   
