# Step 1: Take user input
user_input = input("Enter something: ")

# Step 2: Write input to output.txt
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 3: Append additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Step 4: Read and display final content
with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal Content of output.txt:")
    print(content)
