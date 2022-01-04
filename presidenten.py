import os
import time
import sys
from Game import Game
clear = lambda: os.system('clear')
clear()

developer_mode = False
if len(sys.argv) != 1:
    if sys.argv[1] == "dev":
        developer_mode = True

def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
