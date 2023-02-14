import random


class pabj:
    def __init__(self, name):

        self.name = name
        self.gladness = 24
        self.progress = 2
        self.alive = True
        self.mone = 5

    def to_study (self):
        print("Time to study")
        self.progress += 0.2
        self.gladness -= 2
        if self.progress >= 4:
            self.work()
        elif self.mone >= 10:
            self.progress += 0.3
            self.mone -= 20

    def to_chill(self):
        print("Rest time")
        if self.gladness <= 60:
            self.gladness += 2
            self.progress -= 0.1
            self.mone -= 10
        else:
            self.to_study()

    def work(self):
        print("The work is done")
        self.gladness -= 1
        self.progress -= 0.4
        self.mone += 8

    def is_alive(self):
        if self.progress < -0.3:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress < 3:
            print("Passed externally...")
            self.alive = False
        elif self.mone <= -20:
            print("Duty")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money ={self.mone}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^60}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()

        elif live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.work()
        self.end_of_day()
        self.is_alive()

nick = pabj(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)