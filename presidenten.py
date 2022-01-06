import os
import time
import sys
from game import Game
clear = lambda: os.system('clear')
clear()


def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
