import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize the main application window
root = tk.Tk()
root.title("Personal Diary")
root.geometry("700x600")
root.configure(bg="#2b2d42")  # Dark background for a modern feel

# Function to save the diary entry
def save_entry():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        # Save the entry with the current date as the filename
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"Diary_{date_str}.txt"
        with open(filename, "w") as file:
            file.write(content)
        # Update confirmation label
        confirmation_label.config(text=f"Entry saved as {filename}!", fg="#4caf50")
        text_area.delete("1.0", tk.END)  # Clear the text area after saving
    else:
        confirmation_label.config(text="The diary entry is empty!", fg="#e63946")

# GUI Layout
# Header Label
header_label = tk.Label(
    root, 
    text="Dear Diary", 
    bg="#2b2d42", 
    fg="#f1faee", 
    font=("Poppins", 24, "bold")
)
header_label.pack(pady=10)

# Subheader for Date and Time
date_time_label = tk.Label(
    root, 
    text=datetime.now().strftime("%A, %B %d, %Y - %I:%M %p"), 
    bg="#2b2d42", 
    fg="#8d99ae", 
    font=("Poppins", 14)
)
date_time_label.pack(pady=5)

# Text Area for Writing
text_area = tk.Text(
    root, 
    font=("Poppins", 14), 
    bg="#3a3d4d", 
    fg="#f1faee", 
    insertbackground="#f1faee", 
    wrap=tk.WORD, 
    height=20, 
    width=50
)
text_area.pack(padx=20, pady=10)

# Confirmation Label
confirmation_label = tk.Label(
    root, 
    text="", 
    bg="#2b2d42", 
    fg="#8d99ae", 
    font=("Poppins", 12)
)
confirmation_label.pack(pady=5)

# Save Button
save_button = tk.Button(
    root, 
    text="Save Entry", 
    command=save_entry, 
    bg="#4caf50", 
    fg="#ffffff", 
    font=("Poppins", 14, "bold"), 
    activebackground="#81c784"
)
save_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
