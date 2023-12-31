import time
import random

class SlotsGame:
    cherry = "\U0001F352"  # Unicode for cherry emoji
    lemon = "\U0001F34B"   # Unicode for lemon emoji
    bell = "\U0001F514"    # Unicode for bell emoji

    def __init__(self, casino_profile):
        self.casino_profile = casino_profile
        self.playing = True

    def place_bet(self):
        while True:
            try:    # attempts to convert input to an integer
                amount = int(input("Enter your bet amount: "))
                if amount > 0:
                    return amount
                else:
                    print("Please enter a positive bet amount.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    
    def play(self):
        while self.playing:
            print("\n\n\n---------\n| SLOTS |\n---------")
            self.casino_profile.display_balance()   # calls the display_balance method from CasinoGame that we passed into SlotsGame
            amount = self.place_bet()
            print(f"You have placed a bet of ${amount}")

            # slot machine logic
            symbols = [self.cherry, self.lemon, self.bell]
            result = [random.choice(symbols) for i in range(3)]
            winnings = 0

            print(f"\nSlot Machine Result: \n")
            for i in result:
                print(f"|{i}|", end=" ", flush=True)
                time.sleep(0.5)
            
            if result.count(result[0]) == 3:
                winnings = amount * 10
                print(f"\nCongratulations! You won ${winnings}!")
            else:
               print("\nSorry, you lost.")

            self.casino_profile.balance += winnings - amount
            self.casino_profile.display_balance()

            # check if the balance is negative
            if self.casino_profile.balance < 0:
                print("\nYour balance is negative. Exiting the game.")
                time.sleep(1)
                break

            # ask the user if they want to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("\nExiting the Slots game.")
                self.playing = False
