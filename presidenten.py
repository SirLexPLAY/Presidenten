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
    def __init__(self, name, index, deck):
        self.name = name
        self.index = index
        self.deck = deck
        self.place = 0  # 2: President, 1: Vice President, 0: Nøytral, -1: Vice Boms, -2: Boms



class Game:
    def __init__(self):
        self.message = None
        self.order_of_cards = [3,4,5,7,8,9,10,11,12,13,1,2]


    def exit(self):
        """
        Metode som avlsutter spiller med en fin melding.
        """
        clear()
        print("Thank you for playing!")
        print("© 2021-2022 Made by Dawid Sz.")
        print()
        quit()


    def main_menu(self):
        """
        Hovedmeny metoden. Lar spilleren opprette nytt eller laste inn gammelt spill,
        stille inn innstillinger eller gå ut av spillet.
        """
        if self.message is not None:
            print(self.message + "\n")
            self.message = None

        print("Velkommen til Presidenten!")
        print("Hva vil du gjøre?")
        print("1. Starte nytt spill")
        print("2. Laste inn et spill (INDEV)")
        print("3. Innstillinger (INDEV)")
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
            self.message = "Denne funksjonen er under utvikling!"

        elif choice == 4:
            self.exit()


    def common_num_freq(self, deck):
        """
        Metoden returnerer frekvensen av typetall "kortet"
        """
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


    def is_greater(self, card1, card2):
        """
        Metoden sjekker om kort1 er større enn kort2.
        Tar høyde for at 2 er større enn 3 også videre.

        Returnerer True/False, om kortet er større/mindre.
        """
        index1 = self.order_of_cards.index(card1)
        index2 = self.order_of_cards.index(card2)

        return index1 > index2


    def nice_convert(self, card):
        """
        Metoden tar inn kortet og gir den en finere formatering.
        Returnerer formatert symbol og verdi.
        """
        symbols = {'club':'♣', 'spade':'♠', 'heart':'♥', 'diamond':'♦'}
        values = {1:'A', 11:'J', 12:'Q', 13:'K'}

        sym = symbols[card[0]]
        val = card[1]
        if val in [1] + list(range(11,14)):
            val = values[card[1]]

        return sym, val


    def nice_print(self, deck, chosen):
        """
        Tar inn liste (bunke) med kort.
        Printer dem ut i konsollen med en finere formatering.
        """
        print("Dette er dine kort: \n")
        for i in range(len(deck)):
            sym, val = self.nice_convert(deck[i])

            if i in chosen:
                string = f'> {i+1:2}. {sym}{val}'
            else:
                string = f'  {i+1:2}. {sym}{val}'

            print(string)
        print("")


    def help(self):
        """
        Methoden printer ut en hjelp-melding som beskriver hvordan man spiller.
        """
        clear()
        print("For å velge et kort, skriv kortnummeret og bekreft med ENTER.")
        print("For å angre, skriv kortnummeret til kortet du vil angre på, og bekreft med ENTER.")
        print("For å bekrefte valget ditt, skriv 'FERDIG', og bekreft med ENTER.")
        print("Hvis du ønsker å passere, skriv 'PASSER', og bekreft med ENTER.")
        print()
        input("Klikk ENTER for å komme tilbake til spillet...")


    def is_int(self, str):
        """
        Hjelpemetode for å sjekke om en strenge inneholder kun siffre.
        """
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in str:
            if i not in numbers:
                return False

        return True


    def valid_choice(self):
        """
        Metode som utfra omstendighetene (hvor mange kort runden spilles på,
        hvilke kort som spillere er på vei til å legge ut) bestemmer om spilleren
        har lagt ut en lovlig kombinasjon av kort.
        Returnerer True/False hvis kombinasjonen er lovlig/ulovlig.
        """
        # SJEKK OM SISTE KORTET FRA BUNKEN TIL SPILLEREN SOM ER BLITT LAGT UT ER KLØVER 3
        if len(self.players[self.player_index].deck) == 1:
            if self.players[self.player_index].deck[self.chosen[0]] == ("club", 3):
                self.message = "Spillet kan ikke avsluttes med ♣3!"
                return False

        # SJEKK OM DET ER KLØVER 3 HVIS DET BLE LAGT UT FLERE ENN ET KORT
        if len(self.chosen) > 1:
            for i in self.chosen:
                if self.players[self.player_index].deck[i] == ("club", 3):
                    self.message = "♣3 kan kun legges ut alene!"
                    return False

        # SJEKK OM KLØVER 3 BLE LAGT UT ALENE
        if self.players[self.player_index].deck[self.chosen[0]] == ("club", 3) and len(self.chosen) == 1:
            self.players[self.player_index].place = -2
            self.players_left.remove(self.player_index)
            return True

        # SJEKK OM SPILLEREN HAR VALGT RIKTIG ANTALL KORT
        if not self.first_move:  # Gjelder for alle andre spillere
            if len(self.chosen) < self.round_type:
                self.message = "Du har valgt for få kort!"
                return False
            if len(self.chosen) > self.round_type:
                self.message = "Du har valgt for mange kort!"
                return False
        elif len(self.chosen) > self.max_cards:  # Gjelder kun for den første spilleren i runden
            self.message = "Du har valgt for mange kort!"
            return False

        # SJEKK OM KORTENE SPILLEREN VIL LEGGE UT HAR SAMME VERDI
        cards = []
        for i in self.chosen:
            cards.append(self.players[self.player_index].deck[i])

        values = list(list((zip(*cards)))[1])
        jokers = 0  # Teller antall jokere
        while 6 in values:
            jokers += 1
            values.remove(6)

        if len(values) > 1:
            for i in range(len(values)-1):
                if not values[i+1] == values[i]:
                    self.message = "Du har valgt kort med ulike verdier!"
                    return False

        # SJEKK OM VERDIEN ER HØYERE ENN VERDIEN FRA FORRIGE SPILLER
        if not self.first_move:
            last_move = self.history[-1]
            last_move_value = 0
            for card in last_move:
                if card[1] != 6:
                    last_move_value = card[1]
            if self.is_greater(last_move_value, values[0]):
                self.message = "Du må velge kort med høyere verdi enn det forrige spiller har lagt ut!"
                return False

        return True


    def make_move(self):
        """
        Metode som legger ut kortene med de indeksene som er i self.chosen.
        """
        cards = []
        self.chosen.sort(reverse=True)
        for i in self.chosen:
            cards.append(self.players[self.player_index].deck.pop(i))

        self.history.append(cards)
        self.chosen = []

        if ("club", 3) in cards:
            self.first_move = True
        elif self.first_move:
            self.first_move = False
            self.next_player()
        else:
            self.next_player()


    def check_all_passed(self):
        """
        Metode som sjekker hvis alle har passert.
        """
        if len(self.players_left)-1 <= len(self.has_passed):
            self.has_passed = []
            self.first_move = True


    def next_player(self):
        """
        Metode som setter indexen til den neste spilleren som er i spillet.
        """
        if self.player_index >= self.players_left[-1]:
            for i in self.players_left:
                if i not in self.has_passed:
                    self.player_index = self.players_left[0]
                    self.player_done = True
                    return
        else:
            for i in self.players_left:
                if i > self.player_index and i not in self.has_passed:
                    self.player_index = i
                    self.player_done = True
                    return


    def play_round(self):
        """
        Metode som utfører algoritmen for en runde.
        """
        clear()
        print(f"Nå er det {self.players[self.player_index].name} som spiller!")
        print(f"self.chosen: {self.chosen}")
        self.max_cards = self.common_num_freq(self.players[self.player_index].deck)
        self.nice_print(self.players[self.player_index].deck, self.chosen)
        if self.first_move:
            print(f"Hva vil du gjøre? Du kan starte spillet med {self.max_cards} kort.")
        else:
            print(f"Forrige kort som ble lagt ut er: ", end="")
            for card in self.history[-1]:
                sym, val = self.nice_convert(card)
                print(f"{sym}{val} ", end="")
            print()
            print(f"Hva vil du gjøre? Du må legge ut {self.round_type} kort.")
        print(f"Skriv 'HJELP' for å få opp en liste med kommandoer.")
        if self.message is not None:
            print(self.message)
            print()
            self.message = None
        option = input("> ")

        is_int = self.is_int(option)

        if option == "":
            pass
        elif not is_int:
            if option.lower() == "hjelp":
                self.help()
            elif option.lower() == "ferdig":
                if self.first_move:
                    self.round_type = len(self.chosen)
                if self.valid_choice():
                    self.make_move()
            elif option.lower() == "passer":
                self.chosen = []
                self.has_passed.append(self.player_index)
                self.next_player()
        else:
            option = int(option)-1  # Konverteret kortnummer til index
            amount_cards = len(self.players[self.player_index].deck)

            if len(self.chosen) < self.max_cards:
                if option in range(amount_cards+1) and option not in self.chosen:
                    self.chosen.append(option)
                elif option in range(amount_cards+1) and option in self.chosen:
                    self.chosen.remove(option)
            elif len(self.chosen) >= self.max_cards and option in self.chosen:
                self.chosen.remove(option)
            else:
                self.message = "Du kan ikke velge mellom flere kort."
        self.check_all_passed()


    def run_game(self):
        """
        !!!DENNE METODEN MÅ FIKSES PÅ!!!
          > INNEHOLDER IKKE self.players_left
        """
        clear()
        for i in range(len(self.players)):
            if i not in self.has_passed:
                self.player_done = False    # False = spilleren er ikke ferdig, True = spilleren er ferdig
                while not self.player_done:
                    self.play_round()


    def init_game(self, number_of_players):
        """
        Metoden tar inn antall spillere, så ber spillere om inputs.
        Oppretter spillere, kortbunkene, setter standard innstillinger og
        kjører en while-løkke til spillet er slutt.
        """
        clear()
        self.players = []
        deck = Deck()
        deck.shuffle()
        deck.split(number_of_players)
        self.players_left = []    # Indekser over spiller som er inne i spillet

        for i in range(number_of_players):
            clear()
            print(f"Name of player {i+1}:")
            name = input("> ")
            self.players.append(Player(name, i, deck.decks[i]))
            self.players_left.append(i)

        self.game_state = True    # Spiller er spilt
        self.history = []         # Historikk av alle kort som ble lagt ut
        self.chosen = []          # Hvilke kort som ble valgt av spilleren.
        self.round_type = 0       # Runden spilles 1=enkelt, 2=dobbelt, 3=trippelt, 0=ikke angitt
        self.first_move = True    # Hvis True: spilleren er den første i runden
        self.has_passed = []      # Indekser over spillere som har passert
        self.player_index = 0     # Indeksen til spiller som spiller runden

        while self.game_state:
            self.run_game()


def main():
    game = Game()

    while True:
        clear()
        game.main_menu()


if __name__ == "__main__":
    main()
