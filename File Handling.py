with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","w") as file:
        #This mode allows the user to read as well as write in the file. But it will do the overwriting on the content before.
    file.write("Hello, this is a basic file handlign example using 'with'.\n")
    file.write("Using 'with' ensure the file is properply closed.\n")
    
with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","r") as file:
        #This mode allows the user only to read the file.
    content = file.read()
    print(content)
    
with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","a") as file:
        #This allows the user to add there text to the file without overwriting the previous content.
    file.write("The code looks much clean and readble with using of 'with'.\n")
    
with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","w+") as file:
        #This allows the user to read as well as write the file. But here the previous content will be get erased.
    file.write("Thank You\n")

with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","a+") as file:
        #Opens the file for appending and reading. Creates a new file if it doesn’t exist.
    file.write("Visit again.")
    
with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","rb") as file:
        #Opens the file for reading binary data. File must exist; otherwise, it raises an error.
    content = file.read()
    print(content)
    
with open ("D:\PYTON PROGRAMMING\PYTHON FILES\File IO\example.txt","rb+") as file:
        #Opens the file for both reading and writing binary data. File must exist; otherwise, it raises an error.
    binary_data = file.read()
    print("Existing data:", binary_data)

        # Write new binary data
    new_data = b"\x00\x01\x02\x03"
    file.write(new_data)
    print("Written data:", new_data)

        # Move the file pointer to the beginning
    file.seek(0)

        # Read all data after writing
    updated_data = file.read()
    print("Updated data:", updated_data)



    
    