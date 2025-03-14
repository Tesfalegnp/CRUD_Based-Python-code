import mysql.connector
#to conncted with database
con=mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="python"
    )
if con:
       print("Connected")
else:
    print("not connceted") 
    #Wrire Meno Messahe
    
print("\tMenu Option\n\t 1-register\n\t 2-Display\n\t 3-Search\n\t 4-Delete\n\t 5-update")

ch=input("Please Enter your Choice:- ")
cho=int(ch)

#Match is insted of Switch other program 
if cho==1: 
        name=input("Please enter your name")
        email=input("Please Enter your Email")
        passowrd=input("enter your password")
        sql="INSERT INTO users ('username', 'email', 'password') Values(%s,%s,%s)"
        valu=(name,email,passowrd)
        cor=con.cursor()
        cor.execute(sql,valu)
        con.commit()
        if(cor.rowcount):
            print("inserted________")
        else:
            print("Not Enserted")
        
        
elif cho==2:
    
    print("Displaying")
elif cho==3:
    print("Searching")
elif cho==4:
    print("Deleting")
elif cho==5:
    print("Updating")