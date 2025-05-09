try:
    name = input("Entre your name: ")
    formatted_name = name.title()
    email = input("Entre your email: ")
    age = int(input("Entre your age: "))
    
    if age <= 0 :
        raise ValueError("Invalid Input!") 
    # Raise an error if the age is string , float or negetive integer including zero.
    file = "Bio-Data.txt"
    with open (file,"w") as f:
        f.write("Name- " + formatted_name + "\n" + "Email- "+ email + "\n" + "Age- " + str(age))
        
    with open (file,"r") as f:
        content = f.read()
        print(content)

except ValueError as e:
    print("Error - ",e)


            
    
