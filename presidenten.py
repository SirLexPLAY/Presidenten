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
        for s in ('Ruter', 'Hjerter', 'Spar', 'Kløver'):
            for v in range(1, 14):
                self.cards.append((s,v))


    def shuffle(self):
        """
        Stokker paa kortene.
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


class Game:
    def __init__(self):
        self.message = None


    def main_menu(self):
        print("Velkommen til Presidenten!")
        print("Hva vil du gjøre?")
        print("1. Starte nytt spill")
        print("2. Laste inn et spill (INDEV)")
        print("3. Innstillinger")
        print("4. Gå ut av spillet")
        choice = input("> ")

        if choice == 1:
            return
        elif choice == 2:
            self.message = "Denne funksjonen er under utvikling!"
        elif choice == 3:
            return
        elif choice == 4:
            quit()
        
        if self.message != None:
            print(self.message)


    def hand_out(self):
        return



game = Game()
while True:
    game.main_menu()
    game.message = None
    clear()

bunke = Deck()
bunke.shuffle()
