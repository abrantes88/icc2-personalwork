print ("Menu")  
print ("1) Read and display names") 
print ("2) Add a new name") 
print ("3) Exit")

user = input("Select the menu option:") 
print(user)

if user == "1":
   with open ('names.txt' , 'r') as file:
    print (file.read())   
elif user == "2":
    add_name = input ("Enter the name you want to add:") 
    with open ('names.txt' , 'a') as file:
       file.write(add_name + "\n") 
       print("Name added successfully")
elif user == "3":
   print("Exiting menu...")

       
