import tkinter as tk
from tkinter import messagebox

def show_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Greeting", "Hi, Welcome Again!")

if __name__ == "__main__":
    show_message()
