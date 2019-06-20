from Game.player import Player
from Game.enemy import Enemy, Troll, Vampyre, VampyreKing

tim = Player("Tim")

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

dracula = Vampyre("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

viago = VampyreKing("Viago")
viago.take_damage(12)
print(viago)
