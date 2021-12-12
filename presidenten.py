import os
import time
from Game import Game
clear = lambda: os.system('clear')
clear()


def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
