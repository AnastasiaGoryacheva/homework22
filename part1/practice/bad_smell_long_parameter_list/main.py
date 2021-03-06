# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord, type_of_move, speed=1):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type_of_move = type_of_move
        self.speed = speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + speed, x=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - speed, x=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + speed, unit=self)

    def _get_speed(self):
        if self.type_of_move == 'fly':
            return self.speed * 1.2
        elif self.type_of_move == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Допустимые способы передвижения: летать, ползать!')
