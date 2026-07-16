import tkinter as tk
from tkinter import messagebox
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        self.new_game()

        title = tk.Label(
            root,
            text="🎯 Number Guessing Game",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        title.pack(pady=10)

        info = tk.Label(
            root,
            text="Guess a number between 1 and 100",
            font=("Arial", 12)
        )
        info.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        guess_btn = tk.Button(
            root,
            text="Check Guess",
            font=("Arial", 12),
            command=self.check_guess,
            bg="green",
            fg="white",
            width=15
        )
        guess_btn.pack()

        self.result = tk.Label(
            root,
            text="",
            font=("Arial", 13, "bold")
        )
        self.result.pack(pady=15)

        self.attempt_label = tk.Label(
            root,
            text="Attempts: 0",
            font=("Arial", 12)
        )
        self.attempt_label.pack()

        restart_btn = tk.Button(
            root,
            text="New Game",
            command=self.restart,
            bg="orange",
            fg="white",
            width=15
        )
        restart_btn.pack(pady=15)

    def new_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempt_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.number:
            self.result.config(text="⬇ Too Low!", fg="red")

        elif guess > self.number:
            self.result.config(text="⬆ Too High!", fg="red")

        else:
            self.result.config(
                text=f"🎉 Correct! You guessed it in {self.attempts} attempts.",
                fg="green"
            )
            messagebox.showinfo(
                "Congratulations",
                f"You guessed the number {self.number} in {self.attempts} attempts!"
            )

    def restart(self):
        self.new_game()
        self.entry.delete(0, tk.END)
        self.result.config(text="")
        self.attempt_label.config(text="Attempts: 0")


root = tk.Tk()
app = GuessingGame(root)
root.mainloop()