import tkinter as tk
from tkinter import ttk
import math
import subprocess
import os
import random

# Function to run the pygame script
def run_pygame(script_path):
    try:
        subprocess.Popen(['python', script_path])
    except Exception as e:
        print("Error:", e)

def show_buttons():
    global user_name
    user_name = name_input.get()  # Get user's name from the input field

    # Hide the name input and label
    name_label.place_forget()
    name_entry.place_forget()
    name_submit_button.place_forget()

    # Show welcome message and user name label
    welcome_label.place(x=root.winfo_width() // 2, y=20, anchor="center")  # Top middle
    user_name_label.config(text=f"User: {user_name}")
    user_name_label.place(x=600, y=50, anchor="w")

    # Create buttons in a systematic layout
    button_positions = [
        (375, 200, "Stock Simulator", 'F:/pycharm prj web/stocks/STONKS.py', "black"),
        (375, 275, "Snake and Ladder", 'F:/pycharm prj web/Snake and ladder/main.py', "black"),
        (375, 350, "Flappy Bird", 'F:/pycharm prj web/old-flappy-bird/main.py', "black"),
        (375, 425, "Space Shooter", 'F:/pycharm prj web/SpaceShooter/main.py', "black"),
        # (700, 475, "Exit", root.quit, "black"),
    ]

    for x, y, text, path, color in button_positions:
        button = tk.Button(root, text=text, command=lambda p=path: run_pygame(p), bg=color,
                           font=("Arial", 14), foreground="white", relief="solid", borderwidth=5)
        button.place(x=x, y=y, anchor="center")

# Create the Tkinter window
root = tk.Tk()
root.title("Pygame Launcher")
root.geometry("750x500")  # Set window dimensions
root.configure(bg="black")  # Set background color to black

# Create a canvas for background animation
canvas = tk.Canvas(root, width=750, height=500, bg="black")
canvas.pack()

# Animation: Rotate and draw twinkling stars on the canvas
def draw_twinkling_stars(angle=0):
    canvas.delete("all")  # Clear the canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    star_count = 100
    star_radius = 2

    for _ in range(star_count):
        x = random.randint(0, canvas_width)
        y = random.randint(0, canvas_height)
        alpha = random.randint(50, 255)  # Random opacity value
        fill_color = f"#{alpha:02X}{alpha:02X}{alpha:02X}"
        star = canvas.create_oval(x - star_radius, y - star_radius, x + star_radius, y + star_radius, fill=fill_color)
        canvas.tag_bind(star, "<Enter>", lambda event, s=star: canvas.itemconfig(s, fill="white"))
        canvas.tag_bind(star, "<Leave>", lambda event, s=star: canvas.itemconfig(s, fill=fill_color))

    root.after(500, draw_twinkling_stars)  # Call this function after 500ms

draw_twinkling_stars()  # Start the twinkling star animation

# Get user's name input
name_input = tk.StringVar()
name_label = ttk.Label(root, text="Enter Your Name:", font=("Arial", 12), foreground="white", background="black")
name_label.place(x=10, y=10)
name_entry = ttk.Entry(root, textvariable=name_input, font=("Arial", 12))
name_entry.place(x=150, y=10)

# Create a submit button for the name
name_submit_button = tk.Button(root, text="Submit", command=show_buttons, font=("Arial", 12), foreground="white", bg="black")
name_submit_button.place(x=330, y=10)

# Display user's name with a welcome message
welcome_label = ttk.Label(root, text="Welcome to Pygame Launcher", font=("Arial", 18), foreground="white", background="black")

# Display user's name
user_name_label = ttk.Label(root, text="", font=("Arial", 12), foreground="white", background="black")

# Start the Tkinter event loop
root.mainloop()
