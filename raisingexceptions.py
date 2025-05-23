class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think i'll just walk")


class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)
    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on it, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and brought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
        # if type(duck) is Duck:
        # if isinstance(duck, Duck):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a "+ str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate")  # TODO remove this before release
            except AttributeError as e:
                print('one duck down')
                problem = e
                #raise
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    flock = Flock()
    donald = Duck()
    flock.add_duck(donald)
    flock.migrate()
