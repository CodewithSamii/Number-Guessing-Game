import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")
        master.geometry("400x500")
        master.resizable(False, False)
        master.configure(bg="#2C3E50")

        self.max_attempts = 7
        self.attempts = 0
        self.secret_number = None

        master.bind('<Return>', lambda event: self.check_guess())

        self.title_label = tk.Label(
            master,
            text="Guess the Number!",
            font=("Helvetica", 20, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.title_label.pack(pady=15)

        self.instruction_label = tk.Label(
            master,
            text="I'm thinking of a number between 1 and 100.\nYou’ve got 7 tries!",
            font=("Arial", 14),
            fg="#ECF0F1",
            bg="#2C3E50",
            justify=tk.CENTER
        )
        self.instruction_label.pack(pady=10)

        self.input_frame = tk.Frame(master, bg="#2C3E50")
        self.input_frame.pack(pady=20)

        self.guess_entry = tk.Entry(
            self.input_frame,
            font=("Arial", 16),
            width=26,
            justify=tk.CENTER
        )
        self.guess_entry.pack(pady=(0, 8), ipady=3)

        self.guess_button = tk.Button(
            self.input_frame,
            text="Guess",
            font=("Arial", 14),
            command=self.check_guess,
            bg="#3498DB",
            fg="#ECF0F1",
            activebackground="#2980B9",
            width=10
        )
        self.guess_button.pack(ipady=1)

        self.feedback_label = tk.Label(
            master,
            text="",
            font=("Arial", 14),
            fg="#E74C3C",
            bg="#2C3E50",
            wraplength=400,
            justify=tk.CENTER
        )
        self.feedback_label.pack(pady=15)

        self.remaining_label = tk.Label(
            master,
            text=f"Attempts remaining: {self.max_attempts}",
            font=("Arial", 12),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.remaining_label.pack(pady=5)

        self.reset_button = tk.Button(
            master,
            text="Play Again",
            font=("Arial", 14),
            command=self.reset_game,
            bg="#27AE60",
            fg="#ECF0F1",
            activebackground="#1E8449",
            width=12
        )
        self.reset_button.pack(pady=20)

        self.start_game()

    def start_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_button.config(state=tk.NORMAL)
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.update_remaining_label()

    def update_remaining_label(self):
        left = self.max_attempts - self.attempts
        self.remaining_label.config(text=f"Attempts remaining: {left}")

    def check_guess(self):
        guess = self.guess_entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="Please type a number.")
            return

        guess = int(guess)
        self.attempts += 1
        left = self.max_attempts - self.attempts

        if guess < self.secret_number:
            self.feedback_label.config(text=f"Too low! {left} tries left.")
        elif guess > self.secret_number:
            self.feedback_label.config(text=f"Too high! {left} tries left.")
        else:
            self.feedback_label.config(text=f"You got it! Took you {self.attempts} tries.")
            self.guess_button.config(state=tk.DISABLED)
            return

        if left <= 0:
            self.feedback_label.config(text=f"No more tries! The number was {self.secret_number}.")
            self.guess_button.config(state=tk.DISABLED)

        self.guess_entry.delete(0, tk.END)
        self.update_remaining_label()

    def reset_game(self):
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
