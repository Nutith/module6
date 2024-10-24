class Horse:
    sound = 'Frrr'

    def __init__(self):
        self.x_distance = 0
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        self.sound = Eagle.sound
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
