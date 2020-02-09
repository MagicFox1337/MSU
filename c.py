class Monsters:
    def __init__(self, name, d, h):
        self.name = name
        self.d = d
        self.h = h

    def die(self):
        self.h = 0
        print("Убит монстр", self.name)

    def damage(self, pers):
        pers.h = pers.h - self.d

    def print_info(self):
        print("Удар:", self.d)
        print("Здоровье:", self.h)


class Men:
    def __init__(self, name, d, h, a):
        self.name = name
        self.d = d
        self.h = h
        self.s = False

    def print_info(self):
        print("Удар:", self.d)
        print("Здоровье:", self.h)
        print("Щит:", self.a)

    def die(self):
        self.h = 0
        print("Персонаж", self.name, "убит!")


class Player(Men):
    def heal(self, n):
        self.h = self.h + n
        
    def damage(self, pers):
        pers.h = pers.h - self.d

    def s_attack(self, pers):
        pers.h = pers.h - (self.d*2)

# функция в которой происходит бой
# в нее передается игрок и монстр
def battle(pers, monstr):
    action(pers)
    while True:
        pers.damage(monstr)
        if pers.h <= 0:
            pers.die()
            return pers
        if pers.s == True:
            pers.s = False
        else:
            monstr.damage(pers)
        if monstr.h <= 0:
            monstr.die()
            return monstr

# функция с различными действиями
def action(pers):
    print("1 - лечиться")
    print("2 - увеличить урон")
    print("3 - взять щит")
    option = int(input(">>>"))
    if option == 1:
        pers.h = pers.h + 5
    elif option == 2:
        pers.h = pers.h + 5
    elif option == 3:
        pers.s = True
    else:
        print("Неизвестная команда")

# Создание игрока
name = input("Имя игрока: ")
player = Player(name, 5, 25, False)

print("Приветствую вас,", player.name, "! Приготовьтесь к путешествию!")
print("Вас ждут бои с монстрами!")
print("#########################")

# Сражения
monster1 = Monsters("Гоблин", 5, 25)

battle(player, monster1)

monster2 = Monsters("Тролль", 10, 35)

battle(player, monster2)

monster3 = Monsters("Оборотень", 20, 35)

battle(player, monster3)

monster4 = Monsters("Вампир", 25, 40)

battle(player, monster4)

# Итоги игры
print("#########################")
print("Игра завершена!")













