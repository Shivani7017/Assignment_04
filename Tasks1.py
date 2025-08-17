#WAP the Read a File and Handle Errors 
try:
    with open("sample.txt",'r',encoding="utf-8") as file :
        print("File found! Printing contents:\n")
        for line in file:
          print(line,end="")
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

