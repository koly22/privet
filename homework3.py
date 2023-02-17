import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 23
        self.gladness = 12
        self.satiety = 45
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)

    def date(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        if self.money >= 30:
            self.money -= 20
            self.satiety += 10
            self.gladness += 5
        else:
            pass

    def relatives(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 30:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money -= 10
        self.gladness += 5

    def get_job(self):
        if self.car.drive():
@@ -47,32 +77,32 @@
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 180
            self.car.fuel += 180
        elif manage == "food":
            print("Bought food")
            self.money -= 45
            self.home.food += 45
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.gladness += 5
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.gladness += 5
        self.home.mess += 5

    def clean_home(self):
@@ -105,27 +135,27 @@
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -300:
            print("Bankrupt…")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("a house appeared")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I I need a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        dice = random.randint(1, 6)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
@@ -135,26 +165,32 @@

nick = Human(name="Nick")
for day in range(1,800):
for day in range(800):
    if nick.live(day) == False:
        break