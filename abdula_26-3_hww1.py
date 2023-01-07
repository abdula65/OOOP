class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        return (self.name)

    def hp(self):
        self.health_points *= 2
        return f'Удвоенное здоровье:{self.health_points}'


    def __str__(self):
        return f"{self.superpower}, and the superpower of {self.superpower} and {self.health_points} "

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name='bob', nickname='dod', superpower='bum', health_points='100', catchphrase='lego')
print(hero.__str__())
print(hero.print_name())
print(hero.hp())
print(hero.__len__())
