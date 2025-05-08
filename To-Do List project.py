filename = "To-Do.txt"
print("Enter text (type 'STOP' on a new line to finish):")
with open (filename,"w") as f:
    while True :
        line = input()
        if line.strip().upper() == "STOP":
            break
        f.write(line + "\n")
        
    print(f"Data is been added to {filename}")
    
with open (filename,"r") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines, start=1):
        print(idx,line)
    
    
line_to_remove = int(input("Entre the line you want to mark completed: "))

with open (filename,"w") as f:
    for i, line in enumerate(lines, start=1):
        if i != line_to_remove:
            f.write (line)

    # for idx,line in lines:
    #     if .strip() != line_to_remove.strip():
    #         f.write(line)
            
with open (filename,"r") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines, start=1):
        print("\nUpdated To-Do List:","\n",idx,line)
    
    




    