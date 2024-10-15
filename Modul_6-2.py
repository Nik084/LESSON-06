class Vehicle: # любой транспорт
    __COLOR_VARIANTS = ['WHITE', 'purple', 'gold']
    # print(__COLOR_VARIANTS)
    for j in range(len(__COLOR_VARIANTS)):
        __COLOR_VARIANTS[j] = __COLOR_VARIANTS[j].lower()
    # print(__COLOR_VARIANTS)

    def __init__(self, owner, model, power, color):
        self.owner = str(owner) # Владелец
        self.__model = str(model)
        self.__engine_power = int(power)
        self.__color = str(color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()},\n{self.get_horsepower()},\n{self.get_color()},\nВладелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color.lower() # без .lower() цвет в итоговой строке будет с исх. регистром
        else:
            print(f' (!) Нельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # В седан могут поместиться 5 человек

    pass

vehicle1 = Sedan('Peter', 'VW', 250, 'gray')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('White')
vehicle1.set_color('Pink')
vehicle1.owner = 'Vasyok' # Владелец поменялся
vehicle1.model = 'Audi' # Марка осталась пержней
vehicle1.engine_power = 200 # Мощность осталась прежней

# Проверяем, что поменялось
vehicle1.print_info()
