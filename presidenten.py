# -*- coding: utf-8 -*-
import random
import os
clear = lambda: os.system('clear')
clear()

class Deck:
    def __init__(self):
        """
        Oppretter en vanlig bunke med 52 kort.
        Kortene lar seg dele ut til et objekt av players.

        1 tilsvarer A,
        2-10 tilsvarer vanlige 2-10,
        11 tilsvarer knekt,
        12 tilsvarer dronning,
        13 tilsvarer kongen
        """
        self.cards = []
        self.decks = []
        for s in ('diamond', 'heart', 'spade', 'club'):
            for v in range(1, 14):
                self.cards.append((s,v))


    def shuffle(self):
        """
        Stokker på kortene.
        """
        random.shuffle(self.cards)


    def hand_out(self, n):
        """
        Tar de n foorste kort i en liste,
        fjerner de fra hovedlisten,
        returnerer.
        """
        to_be_handed = []

        for i in range(n):
            to_be_handed.append(self.cards[0])
            self.cards.pop(0)

        return to_be_handed


    def split(self, n):
        """
        Deler ut kortstokken på n antall spillere.
        """
        cards_per_player = int(52/n)
        self.decks = []

        for i in range(n):
            deck = self.hand_out(cards_per_player)
            self.decks.append(sorted(deck, key=lambda x: x[1]))




class Player():
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck



class Game:
    def __init__(self):
        self.message = None


    def exit(self):
        clear()
        print("Thank you for playing!")
        print("© 2021-2022 Made by Dawid Sz.")
        print()
        quit()


    def main_menu(self):
        if self.message is not None:
            print(self.message + "\n")
            self.message = None

        print("Velkommen til Presidenten!")
        print("Hva vil du gjøre?")
        print("1. Starte nytt spill")
        print("2. Laste inn et spill (INDEV)")
        print("3. Innstillinger")
        print("4. Gå ut av spillet")
        choice = input("> ")
        if choice is not "":
            choice = int(choice)

        if choice == "":
            self.message = "Ingenting ble valgt. Prøv på nytt!"

        elif choice == 1:
            clear()

            print("Hvor mange spillere?")
            number_of_players = int(input("> "))
            self.init_game(number_of_players)

        elif choice == 2:
            self.message = "Denne funksjonen er under utvikling!"

        elif choice == 3:
            return

        elif choice == 4:
            self.exit()


    def common_num_freq(self, deck):
        values = list(zip(*deck))[1]

        play = 1
        count = 0
        val = 0
        for i in values:
            if i == val:
                count += 1
                if count > play:
                    play = count

            else:
                val = i
                count = 1

        return play


    def nice_print(self, deck):
        """
        Tar inn liste (bunke) med kort.
        Printer dem ut i konsollen med en finere formatering.
        """
        symbols = {'club':'♣', 'spade':'♠', 'heart':'♥', 'diamond':'♦'}
        values = {1:'A', 11:'J', 12:'Q', 13:'K'}

        print("Dine kort: \n")
        for i in range(len(deck)):
            sym = deck[i][0]
            val = deck[i][1]

            sym = symbols[sym]
            if val in [1] + list(range(11,14)):
                val = values[val]

            string = f'{sym}{val}'
            print(string)


    def run_game(self):
        clear()
        history = []         # Historikk av alle kort som ble lagt ut
        round_type = 0       # Runden spilles 1=enkelt, 2=dobbelt, 3=trippelt, 0=ikke angitt
        first_round = True   # Hvis True: spilleren er den første i runden
        has_passed = []      # Indekser over spillere som har passert

        for i in range(len(self.players)):
            if i not in has_passed:
                if first_round:
                    self.common_num_freq(self.players[i].deck)
                    self.nice_print(self.players[i].deck)
                    exit()


    def init_game(self, number_of_players):
        clear()
        self.players = []
        deck = Deck()
        deck.shuffle()
        deck.split(number_of_players)

        for i in range(number_of_players):
            clear()
            print(f"Name of player {i+1}:")
            name = input("> ")
            self.players.append(Player(name, deck.decks[i]))

        self.game_state = True   # Spiller er spilt

        while self.game_state:
            self.run_game()




def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
