class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def stop(self):
        print('Машина остановилась')
    def change_color(self, new_color):
        self.color = new_color

BYD = Car('Chazor', 'Black', 2023)
BYD.change_color('Gray')
print(BYD.color)