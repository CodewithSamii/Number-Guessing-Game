import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("360x640") 
        self.root.config(bg="lightblue")

        self.max_chances = 7

        # Title and instructions
        tk.Label(root, text="Number Guessing Game", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
        tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12), bg="lightblue").pack()

        # Input box: editable, piped cursor
        self.input_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.input_var, font=("Arial", 20), justify="center", width=6)
        self.display.pack(pady=10)
        self.display.focus_set()  # Enable cursor

        # Number pad (calculator-style)
        self.create_number_pad()

        # Submit button
        self.submit_btn = tk.Button(root, text="Submit", command=self.check_guess,
                                    bg="green", fg="white", width=15, font=("Arial", 12))
        self.submit_btn.pack(pady=10)

        # Feedback labels
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
        self.result_label.pack(pady=10)

        self.chances_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
        self.chances_label.pack()

        # Play again button
        self.play_again_btn = tk.Button(root, text="Play Again", command=self.reset_game,
                                        state='disabled', width=15)
        self.play_again_btn.pack(pady=10)

        # Bind Enter key
        self.root.bind("<Return>", lambda event: self.check_guess())

        # Start a new game
        self.reset_game()

    def create_number_pad(self):
        pad_frame = tk.Frame(self.root, bg="lightblue")
        pad_frame.pack()

        btn_font = ("Arial", 16)
        for i in range(1, 10):
            b = tk.Button(pad_frame, text=str(i), font=btn_font, width=5, height=2,
                          command=lambda x=i: self.append_digit(x))
            row, col = divmod(i - 1, 3)
            b.grid(row=row, column=col, padx=5, pady=5)

        zero_btn = tk.Button(pad_frame, text="0", font=btn_font, width=16, height=2,
                             command=lambda: self.append_digit(0))
        zero_btn.grid(row=3, column=0, columnspan=3, pady=5)

        clear_btn = tk.Button(self.root, text="Clear", font=("Arial", 12),
                              bg="red", fg="white", width=10, command=self.clear_input)
        clear_btn.pack()

    def append_digit(self, digit):
        current = self.input_var.get()
        if len(current) < 3:
            self.input_var.set(current + str(digit))

    def clear_input(self):
        self.input_var.set("")

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.remaining_chances = self.max_chances
        self.input_var.set("")
        self.result_label.config(text="")
        self.chances_label.config(text=f"Chances left: {self.remaining_chances}")
        self.submit_btn.config(state='normal')
        self.play_again_btn.config(state='disabled')
        self.display.config(state='normal')
        self.display.focus_set()

    def check_guess(self):
        guess_str = self.input_var.get()
        if not guess_str.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number between 1 and 100.")
            return

        guess = int(guess_str)
        if guess < 1 or guess > 100:
            self.result_label.config(text="Enter a number between 1 and 100.")
            return

        self.remaining_chances -= 1
        self.chances_label.config(text=f"Chances left: {self.remaining_chances}")

        if guess == self.number:
            self.result_label.config(text=f"You are the Winner! 🎉 The number was {self.number}")
            self.end_game()
        elif abs(guess - self.number) <= 5:
            self.result_label.config(text="Very Close! Try Again 🔍")
        elif guess < self.number:
            self.result_label.config(text="Too Low ⬇")
        else:
            self.result_label.config(text="Too High ⬆")

        if self.remaining_chances == 0 and guess != self.number:
            self.result_label.config(text=f"Out of chances! ❌ The number was {self.number}")
            self.end_game()

        self.input_var.set("")

    def end_game(self):
        self.submit_btn.config(state='disabled')
        self.play_again_btn.config(state='normal')
        self.display.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
