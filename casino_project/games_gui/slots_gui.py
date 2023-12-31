import tkinter as tk
import random
import time
from PIL import Image, ImageTk  # Make sure to install the Pillow library: pip install Pillow

class SlotsGameGUI:
    def __init__(self, master, casino_game, back_callback):
        self.master = master
        self.master.title("Slots Game")
        self.casino_game = casino_game
        self.back_callback = back_callback
        self.symbols = ["cherry.png", "lemon.png", "heart.png"]  # Image file paths

        self.label_balance = tk.Label(self.master, text=self.casino_game.display_balance())
        self.label_balance.pack(pady=10)

        self.label_result = tk.Label(self.master)
        self.label_result.pack(pady=10)

        self.entry_bet = tk.Entry(self.master)
        self.entry_bet.pack(pady=10)

        self.button_spin = tk.Button(self.master, text="Spin", command=self.spin)
        self.button_spin.pack(pady=10)

        self.button_back = tk.Button(self.master, text="Back to Menu", command=self.back_to_menu)
        self.button_back.pack(pady=10)

        # Load images
        self.image_paths = {symbol: Image.open(symbol) for symbol in self.symbols}
        self.images = {symbol: ImageTk.PhotoImage(image) for symbol, image in self.image_paths.items()}

    def spin(self):
        try:
            amount = int(self.entry_bet.get())
            if 0 < amount <= self.casino_game.balance:
                result = [random.choice(self.symbols) for _ in range(3)]
                self.display_result(result)
                winnings = self.calculate_winnings(result, amount)
                self.casino_game.balance += winnings - amount
                self.label_balance.config(text=self.casino_game.display_balance())
            else:
                self.label_result.config(text="Invalid bet amount")
        except ValueError:
            self.label_result.config(text="Invalid bet amount")

    def calculate_winnings(self, result, amount):
        if result.count(result[0]) == 3:
            return amount * 10
        return 0

    def display_result(self, result):
        self.label_result.config(text="")
        self.slowly_reveal_symbols(result, 0)

    def slowly_reveal_symbols(self, symbols, index):
        if index < len(symbols):
            current_symbol = symbols[index]
            self.label_result.config(image=self.images[current_symbol])
            self.master.after(500, self.slowly_reveal_symbols, symbols, index + 1)  # Adjust the delay (in milliseconds)
        else:
            self.check_winning_condition(symbols)

    def check_winning_condition(self, symbols):
        if symbols.count(symbols[0]) == 3:
            self.label_result.config(text=f"Congratulations! You won!")
        else:
            self.label_result.config(text="Sorry, you lost.")

    def back_to_menu(self):
        # Call the back_callback function to show the main menu
        self.back_callback()
        # Destroy the current slots game window
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    casino_game = CasinoGame()
    slots_gui = SlotsGameGUI(root, casino_game)
    root.mainloop()
