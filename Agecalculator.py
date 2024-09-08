import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birthdate = datetime.strptime(entry.get(), "%Y-%m-%d")
        today = datetime.today()
        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day

        if days < 0:
            months -= 1
            previous_month = (today.month - 1) % 12 or 12
            previous_month_year = today.year if previous_month != 12 else today.year - 1
            days_in_prev_month = (datetime(previous_month_year, previous_month + 1, 1) - datetime(previous_month_year, previous_month, 1)).days
            days += days_in_prev_month

        if months < 0:
            years -= 1
            months += 12

        result_label.config(text=f"You are {years} years, {months} months, and {days} days old.")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter the date in the correct format (YYYY-MM-DD)")

root = tk.Tk()
root.title("Age Calculator")

label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to calculate age
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Running the Tkinter event loop
root.mainloop()
