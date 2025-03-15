import tkinter as tk
from tkinter import ttk
import random

class CiparuSpele:
    def __init__(self, root):
        self.root = root
        self.root.title("CIPARU SPĒLE")
        self.root.geometry("1000x500")
        self.player_turn = True
        self.player_score = 0
        self.ai_score = 0
        self.start_screen()

    def start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(container, text="CIPARU SPĒLE", font=("Arial", 24, "bold")).pack()

        frame = tk.Frame(container)
        frame.pack(pady=20)
        tk.Label(frame, text="Ievadiet ciparu skaitu:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)

        self.sequence_length_var = tk.StringVar(value="15")
        self.sequence_dropdown = ttk.Combobox(frame, textvariable=self.sequence_length_var, values=[str(i) for i in range(15, 21)], state='readonly')
        self.sequence_dropdown.pack(side=tk.LEFT)

        tk.Button(container, text="SĀKT SPĒLI", font=("Arial", 14, "bold"), command=self.game_screen).pack(pady=20)

    def game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(container, text="CIPARU SPĒLE", font=("Arial", 24, "bold")).pack()

        self.turn_label = tk.Label(container, text=self.get_turn_text(), font=("Arial", 14))
        self.turn_label.pack(pady=10)

        self.selected_number = tk.IntVar(value=-1)
        sequence_length = int(self.sequence_length_var.get())
        self.sequence = random.choices([1, 2, 3, 4], k=sequence_length)

        sequence_frame = tk.Frame(container)
        sequence_frame.pack(pady=10)

        for index, num in enumerate(self.sequence):
            btn = tk.Radiobutton(sequence_frame, text=str(num), variable=self.selected_number, value=index, indicatoron=0, font=("Arial", 12), padx=5, pady=5)
            btn.pack(side=tk.LEFT, padx=2)

        tk.Button(container, text="DALĪT SKAITLI", font=("Arial", 14)).pack(pady=10)
        tk.Button(container, text="PAŅEMT SKAITLI", font=("Arial", 14)).pack(pady=5)

        score_frame = tk.Frame(container)
        score_frame.pack(pady=20)

        self.player_score_label = tk.Label(score_frame, text=f"Spēlētāja punktu skaits: {self.player_score}", font=("Arial", 12))
        self.player_score_label.pack(side=tk.LEFT, padx=20)

        self.ai_score_label = tk.Label(score_frame, text=f"AI punktu skaits: {self.ai_score}", font=("Arial", 12))
        self.ai_score_label.pack(side=tk.LEFT)

    def get_turn_text(self):
        return "Spēlētāja gājiens" if self.player_turn else "AI gājiens"

if __name__ == "__main__":
    root = tk.Tk()
    game = CiparuSpele(root)
    root.mainloop()