from games.slots import SlotsGame
from games_gui.slots_gui import SlotsGameGUI
import tkinter as tk


class CasinoGame:
    
    def __init__(self, initial_balance=100):
        self.balance = initial_balance

    def display_balance(self):
        print(f"Your current balance: ${self.balance}")


class CasinoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Casino Game")
        self.master.geometry("500x500")  
        self.casino_game = CasinoGame()

        self.label_balance = tk.Label(self.master, text=self.casino_game.display_balance())
        self.label_balance.pack(pady=10)  # Add vertical padding

        # Centered Frame
        frame = tk.Frame(self.master)
        frame.pack()

        self.button_slots = tk.Button(frame, text="Play Slots", command=self.show_slots_gui, width=20, height=3)
        self.button_slots.pack(side="left", padx=10)  # Add horizontal padding

        self.button_exit = tk.Button(frame, text="Exit", command=self.master.destroy, width=20, height=3)
        self.button_exit.pack(side="left", padx=10)  # Add horizontal padding

    def show_slots_gui(self):
        self.master.withdraw()  # Hide the main menu window
        slots_root = tk.Toplevel(self.master)  # Create a new top-level window for the slots game
        slots_gui = SlotsGameGUI(slots_root, self.casino_game, self.show_main_menu)
        slots_root.protocol("WM_DELETE_WINDOW", self.show_main_menu)  # Handle window close event
        slots_root.geometry("400x400")  # Set the window size for the slots game

    def show_main_menu(self):
        self.master.deiconify()  # Show the main menu window
        self.label_balance.config(text=self.casino_game.display_balance())

if __name__ == "__main__":
    root = tk.Tk()
    app = CasinoApp(root)
    root.mainloop()