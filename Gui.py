import tkinter as tk
from tkinter import messagebox


def show_data():
    name = name_entry.get().strip()
    gender = gender_var.get()

    interests = []

    if music_var.get():
        interests.append("Music")

    if sports_var.get():
        interests.append("Sports")

    if not name:
        messagebox.showwarning("Warning", "Please enter your name.")
        return

    if not interests:
        interests.append("None")

    info = (
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Interests: {', '.join(interests)}"
    )

    messagebox.showinfo("User Information", info)


# Create main window
root = tk.Tk()
root.title("User Info Form")
root.geometry("300x300")


# Name
tk.Label(root, text="Enter Name:").pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)


# Gender
tk.Label(root, text="Gender:").pack(pady=5)

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender_var,
    value="Male"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender_var,
    value="Female"
).pack()


# Interests
tk.Label(root, text="Interests:").pack(pady=5)

music_var = tk.BooleanVar()
sports_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Music",
    variable=music_var
).pack()

tk.Checkbutton(
    root,
    text="Sports",
    variable=sports_var
).pack()


# Submit button
tk.Button(
    root,
    text="Submit",
    command=show_data
).pack(pady=15)


# Start the application
root.mainloop()
