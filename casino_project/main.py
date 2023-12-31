from games.slots import SlotsGame
import time


class CasinoGame:
    
    def __init__(self, initial_balance=100):
        self.balance = initial_balance

    def display_balance(self):
        print(f"Your current balance: ${self.balance}")


if __name__ == "__main__":       # ensures the code below is executed only when the script is run directly and not when it's imported as a module
    chad = CasinoGame()          # creates an instance of the CasinoGame class

    while True:

        print("\n\n\n--------------------\n| CASINO GAME MENU |\n--------------------")
        chad.display_balance()
        if chad.balance > 0:
            menu_user_input = input("\nWhich game do you want to play?\n1. Slots\n2. Coming Soon\n3. Exit\n")
            if menu_user_input == "1":
                slots_game = SlotsGame(chad)    # passes the CasinoGame instance to SlotsGame
                slots_game.play()

            elif menu_user_input == "2":
                print("\nThis game is coming soon")
                time.sleep(1)

            elif menu_user_input == "3":
                print("Exiting the casino. Thank you for playing!")
                break

            else:
                print("Invalid input")
                time.sleep(1)
        else:
            print("\nYou lost")
            time.sleep(1)
            break