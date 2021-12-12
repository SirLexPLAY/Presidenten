class Player():
    def __init__(self, name, index, deck):
        self.name = name
        self.index = index
        self.deck = deck
        self.place = 0  # 2: President, 1: Vice President, 0: Nøytral, -1: Vice Boms, -2: Boms
