class Animal:
    alive = 'True #(живой)'
    fed = 'False #(ненакормленный)'
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        self.food = food.name
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = 'True #(накормленный)'
        if food.edible is False:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = 'False #(неживой)'

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    edible = False #(несъедобный)
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True #(съедобный)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
