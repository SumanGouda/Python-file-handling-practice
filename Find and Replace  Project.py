filename = "user_input.txt"
filename1 = "user_input_replaced.txt"

with open (filename,"w") as file:
    print("Enter text (type 'STOP' on a new line to finish):")
    while True :
        line = input()
        if line.strip().upper() == "STOP":
            break
        file.write(line + "\n")
        
print(f"Data written to {filename}")

word = input("Entre the word you want to replace: ")
word_replace = input("Entre the word you want to replace with: ")

with open (filename,"r") as file:
    content = file.read()
    
new_content = content.replace(word,word_replace)

with open (filename1,"w") as file:
    file.write(new_content)
    
print(f"Updated content written to {filename1}")


