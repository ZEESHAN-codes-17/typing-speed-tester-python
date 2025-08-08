import tkinter as tk
from tkinter import messagebox
import random
import time

sentences = [
    "Python is a powerful programming language used in many fields.",
    "Fast typing skills can improve your productivity and workflow.",
    "The quick brown fox jumps over the lazy dog.",
    "Always write clean and readable code to make debugging easier.",
    "Practice makes perfect when it comes to typing and coding.",
    "Artificial Intelligence is shaping the future of technology.",
    "Stay consistent and never give up on your learning journey.",
    "Keyboard shortcuts save time and help you work faster.",
    "Debugging is twice as hard as writing the code in the first place.",
    "Typing speed is measured in words per minute and accuracy."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x400")
        self.root.configure(bg="#22223b")

        self.sentence = random.choice(sentences)
        self.start_time = None
        self.timer_running = False

        self.title_label = tk.Label(root, text="Typing Speed Tester", font=("Arial Black", 22), fg="#f2e9e4", bg="#22223b")
        self.title_label.pack(pady=10)

        self.sentence_label = tk.Label(root, text=self.sentence, font=("Arial", 14), fg="#c9ada7", bg="#22223b", wraplength=650)
        self.sentence_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Consolas", 14), width=70, bg="#4a4e69", fg="#f2e9e4", insertbackground="#f2e9e4")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.timer_label = tk.Label(root, text="Time: 0.00 s", font=("Arial", 14), fg="#9a8c98", bg="#22223b")
        self.timer_label.pack(pady=5)

        self.submit_btn = tk.Button(root, text="Submit", font=("Arial", 14), bg="#9a8c98", fg="#22223b", command=self.calculate_results)
        self.submit_btn.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="#f2e9e4", bg="#22223b")
        self.result_label.pack(pady=10)

        self.reset_btn = tk.Button(root, text="Try Another", font=("Arial", 12), bg="#c9ada7", fg="#22223b", command=self.reset)
        self.reset_btn.pack(pady=5)

        self.update_timer()

    def start_timer(self, event):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True

    def update_timer(self):
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed:.2f} s")
        self.root.after(50, self.update_timer)

    def calculate_results(self):
        if not self.timer_running:
            messagebox.showinfo("Info", "Start typing to begin the test!")
            return
        end_time = time.time()
        time_taken = end_time - self.start_time
        user_input = self.entry.get()
        words_typed = len(user_input.split())
        wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0
        accuracy = (len(set(user_input.split()) & set(self.sentence.split())) / len(self.sentence.split())) * 100
        self.result_label.config(
            text=f"Time Taken: {time_taken:.2f} s\nTyping Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )
        self.timer_running = False

    def reset(self):
        self.sentence = random.choice(sentences)
        self.sentence_label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.timer_label.config(text="Time: 0.00 s")
        self.start_time = None
        self.timer_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()