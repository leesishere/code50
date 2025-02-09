import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Create a label widget with "Hello, World!" text
hello_label = tk.Label(root, text="Hello, World!")
hello_label.pack(pady=20)

# Run the application
root.mainloop()
