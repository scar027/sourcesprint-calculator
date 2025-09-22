import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, messagebox

def calculate_score():
    score = 0

    # Commit message
    if commit_msg_var.get() == "Yes":
        score += 2

    # Description
    if description_var.get() == "Yes":
        score += 3

    # PR type
    pr_type = pr_var.get()
    if pr_type == "Fully Solved":
        score += 10
    elif pr_type == "Partially Solved":
        try:
            partial_points = int(partial_points_var.get())
            if 4 <= partial_points <= 6:
                score += partial_points
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter valid partial points (4-6).")
            return
    elif pr_type == "Failed but Working Code":
        try:
            fail_points = int(fail_points_var.get())
            if 1 <= fail_points <= 3:
                score += fail_points
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter valid fail points (1-3).")
            return

    # Multipliers
    issue_mult = {"Easy": 1, "Medium": 1.5, "Hard": 2}[issue_var.get()]
    repo_mult = {"Easy": 1, "Medium": 1.3, "Hard": 2}[repo_var.get()]

    final_score = score * issue_mult * repo_mult

    result_var.set(f"Final Score: {final_score:.2f}")

def reset_fields():
    commit_msg_var.set("No")
    description_var.set("No")
    pr_var.set("Fully Solved")
    partial_points_var.set("")
    fail_points_var.set("")
    issue_var.set("Easy")
    repo_var.set("Easy")
    result_var.set("Final Score: ")

# ---------------- GUI ----------------
app = ttk.Window(themename="darkly")
app.title("Contribution Score Calculator")
app.geometry("500x700")

# Title
ttk.Label(app, text="Contribution Score Calculator",
          font=("Helvetica", 18, "bold")).pack(pady=15)

# Commit message
ttk.Label(app, text="Proper Commit Message?").pack(pady=5)
commit_msg_var = StringVar(value="No")
ttk.Combobox(app, textvariable=commit_msg_var,
             values=["Yes", "No"], state="readonly").pack()

# Description
ttk.Label(app, text="Proper PR Description?").pack(pady=5)
description_var = StringVar(value="No")
ttk.Combobox(app, textvariable=description_var,
             values=["Yes", "No"], state="readonly").pack()

# PR type
ttk.Label(app, text="Pull Request Type").pack(pady=5)
pr_var = StringVar(value="Fully Solved")
pr_combo = ttk.Combobox(app, textvariable=pr_var,
                        values=["Fully Solved", "Partially Solved", "Failed but Working Code"],
                        state="readonly")
pr_combo.pack()

# Partial points
ttk.Label(app, text="(If Partially Solved) Enter points [4-6]").pack(pady=2)
partial_points_var = StringVar()
ttk.Entry(app, textvariable=partial_points_var).pack()

# Failed points
ttk.Label(app, text="(If Failed but Working Code) Enter points [1-3]").pack(pady=2)
fail_points_var = StringVar()
ttk.Entry(app, textvariable=fail_points_var).pack()

# Issue difficulty
ttk.Label(app, text="Issue Difficulty").pack(pady=5)
issue_var = StringVar(value="Easy")
ttk.Combobox(app, textvariable=issue_var,
             values=["Easy", "Medium", "Hard"], state="readonly").pack()

# Repo difficulty
ttk.Label(app, text="Repository Difficulty").pack(pady=5)
repo_var = StringVar(value="Easy")
ttk.Combobox(app, textvariable=repo_var,
             values=["Easy", "Medium", "Hard"], state="readonly").pack()

# Result
result_var = StringVar(value="Final Score: ")
ttk.Label(app, textvariable=result_var, font=("Helvetica", 16, "bold"),
          bootstyle=SUCCESS).pack(pady=20)

# Buttons
frame = ttk.Frame(app)
frame.pack(pady=10)

ttk.Button(frame, text="Calculate", command=calculate_score,
           bootstyle=PRIMARY).grid(row=0, column=0, padx=10)

ttk.Button(frame, text="New Calculation", command=reset_fields,
           bootstyle=INFO).grid(row=0, column=1, padx=10)

ttk.Button(frame, text="Quit", command=app.quit,
           bootstyle=DANGER).grid(row=0, column=2, padx=10)

app.mainloop()
