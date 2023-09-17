import tkinter as tk
from tkinter import messagebox

def register_user():
    with open('data.txt', 'a') as file:
        file.write(f"First Name: {first_name_entry.get()}\n")
        file.write(f"Second Name: {last_name_entry.get()}\n")
        file.write(f"Username: {username_entry.get()}\n")
        file.write(f"Password: {password_entry.get()}\n")
        file.write(f"Email: {email_entry.get()}\n")
        file.write("-" * 40 + "\n")

    messagebox.showinfo("Success", "User registered successfully!")
    
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Registration Form")


first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)
password_entry = tk.Entry(root, show='*')  # Hide password input with '*'
password_entry.grid(row=3, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)




register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
