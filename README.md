# Python File Handling Programs

This repository contains simple Python programs that demonstrate **file handling concepts**.  
It is beginner-friendly and shows how to write, append, and read data from files.

---

## 📌 Programs Included

### 1. Basic File Handling
- Takes user input and writes it to a file (`output.txt`).
- Appends additional data to the same file.
- Reads and displays the final content.

**Code Example:**
```python
user_input = input("Enter something: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal Content of output.txt:")
    print(content)
