import os

class Player:
    def __init__(self, nickname, hp, max_hp, mana):
        self.p_nickname = nickname
        self.p_hp = hp
        self.p_max_hp = max_hp
        self.p_mana = mana

p1 = Player("Каян", 100, 100, 50)
p2 = Player("Эрен", 100, 100, 50)
p3 = Player("Майлон", 200, 200, 100)

