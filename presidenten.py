# -*- coding: utf-8 -*-
import random
import os
import time
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


    def nice_print(self, deck, chosen):
        """
        Tar inn liste (bunke) med kort.
        Printer dem ut i konsollen med en finere formatering.
        """
        symbols = {'club':'♣', 'spade':'♠', 'heart':'♥', 'diamond':'♦'}
        values = {1:'A', 11:'J', 12:'Q', 13:'K'}

        if self.message is not None:
            print(self.message)
            self.message = None

        print("Dette er dine kort: \n")
        for i in range(len(deck)):
            sym = deck[i][0]
            val = deck[i][1]

            sym = symbols[sym]
            if val in [1] + list(range(11,14)):
                val = values[val]

            if i in chosen:
                string = f'> {i+1:2}. {sym}{val}'
            else:
                string = f'  {i+1:2}. {sym}{val}'

            print(string)
        print("")


    def help(self):
        clear()
        print("For å velge et kort, skriv kortnummeret og bekreft med ENTER.")
        print("For å angre, skriv kortnummeret til kortet du vil angre på, og bekreft med ENTER.")
        print("For å bekrefte valget ditt, skriv 'FERDIG', og bekreft med ENTER.")
        print("Hvis du ønsker å passere, skriv 'PASSER', og bekreft med ENTER.")
        print()
        input("Klikk ENTER for å komme tilbake til spillet...")


    def is_int(self, str):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in str:
            if i not in numbers:
                return False

        return True


    def valid_choice(self, player_index):
        choice_is_valid = True

        # SJEKK OM SPILLEREN HAR VALGT RIKTIG ANTALL KORT
        if not self.first_move and len(self.chosen) == self.round_type:  # Gjelder for alle andre spillere
            return False
        elif len(self.chosen) > self.max_cards:  # Gjelder kun for den første spilleren i runden
            self.message = "Du har valgt for mange kort!"
            return False

        # SJEKK OM KORTENE SPILLEREN VIL LEGGE UT HAR SAMME VERDI
        cards = []
        for i in self.chosen:
            cards.append(self.players[player_index].deck[i])

        values = list(zip(*cards))[1]
        jokers = 0  # Teller antall jokere
        while 6 in values:
            jokers += 1
            values.remove(6)

        if len(values) > 1:
            for i in range(len(values)-1):
                if not values[i+1] == values[i]:
                    self.message = "Du har valgt kort med ulike verdier!"
                    return False



        # SJEKK OM SISTE KORTET FRA BUNKEN TIL SPILLEREN SOM ER BLITT LAGT UT ER KLØVER 3
        if len(self.players[player_index].deck) == 1 and self.chosen[0] == ("club", 3):
            return False

        return True


    def first_round(self, player_index):
        clear()
        self.max_cards = self.common_num_freq(self.players[player_index].deck)
        self.nice_print(self.players[player_index].deck, self.chosen)
        print(f"Hva vil du gjøre? Du kan starte spillet med {self.max_cards} kort.")
        print(f"Skriv 'HJELP' for å få opp en liste med kommandoer.")
        option = input("> ")

        is_int = self.is_int(option)

        if option == "":
            pass
        elif not is_int:
            if option.lower() == "hjelp":
                self.help()
            elif option.lower() == "ferdig":
                self.round_type = len(self.chosen)
                if self.valid_choice(player_index):
                    print("Kombinasjonen er lovlig!")
            elif option.lower() == "passer":
                self.has_passed.append(player_index)
                self.player_done == True
        else:
            option = int(option)-1  # Konverteret kortnummer til index
            amount_cards = len(self.players[player_index].deck)

            if len(self.chosen) < self.max_cards:
                if option in range(amount_cards+1) and option not in self.chosen:
                    self.chosen.append(option)
                elif option in range(amount_cards+1) and option in self.chosen:
                    self.chosen.remove(option)
            elif len(self.chosen) >= self.max_cards and option in self.chosen:
                self.chosen.remove(option)
            else:
                self.message = "Du kan ikke velge mellom flere kort."



    def run_game(self):
        clear()
        for i in range(len(self.players)):
            if i not in self.has_passed:
                self.player_done = False    # False = spilleren er ikke ferdig, True = spilleren er ferdig
                while not self.player_done:
                    if self.first_move:
                        self.first_round(i)




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
        self.history = []         # Historikk av alle kort som ble lagt ut
        self.chosen = []          # Hvilke kort som ble valgt av spilleren.
        self.round_type = 0       # Runden spilles 1=enkelt, 2=dobbelt, 3=trippelt, 0=ikke angitt
        self.first_move = True    # Hvis True: spilleren er den første i runden
        self.has_passed = []      # Indekser over spillere som har passert

        while self.game_state:
            self.run_game()




def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
