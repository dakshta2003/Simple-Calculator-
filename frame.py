import tkinter as tk

# Function to update the expression
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry
def clear():
    entry_var.set("")

# Creating main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")  # Set background color to black

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Creating buttons
for text, row, col in buttons:
    action = lambda x=text: press(x) if x != "=" else calculate()
    tk.Button(root, text=text, font=("Arial", 18), command=action, width=5, height=2, 
              bg="grey", fg="black").grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", font=("Arial", 18), command=clear, width=21, height=2, 
          bg="grey", fg="black").grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the application
root.mainloop()
