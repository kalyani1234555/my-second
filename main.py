# import player

# tim = player.Player("tim")

from player import Player

tim = Player("tim")

print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)

# print(tim.get_name())
# tim.set_lives(300)


from inheritance import Enemy, Troll, Vampyre
random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly_troll - {}".format(ugly_troll))

# another_troll = Troll("Ug", 18, 1, )
# print("Another troll - {}".format(another_troll), end="")

# brother = Troll("Urg", 23)
# print(brother)

ugly_troll = Troll("Pug")
print("Ugly_troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)
ugly_troll.grant()
another_troll.grant()
brother.grant()

# monster = Enemy("Basic Enemy")
# Enemy.grant()

vamp = Vampyre("Vlad")
print(vamp)

vamp.take_damage(5)
print(vamp)

print("_" * 40)
another_troll.take_damage(30)
print(another_troll)

# while vamp.alive:
#     vamp.take_damage(1)
#     print(vamp)

vamp = Vampyre("Vlad")
while vamp._alive:
    if not vamp.dodges():
        vamp.take_damage(1)
    print(vamp)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)

from inheritance challenge import VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
