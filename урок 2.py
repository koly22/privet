import random
class Student:
    def __init__(self, name):

        self.name = name
        self.gladness = 58
        self.progress = 8
        self.alive = True

    def to_study (self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3


    def to_chill(self):

        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):

         if self.progress < -0.5:
         print("Cast out...")
         self.alive = False

    elif self.gladness <= 0:
         print("Depression...")
         self.alive = False
    elif self.progress> 5:
         print("Passed externally..")
         self,alive = False

    def end of day(self):

         print (f"Gladness = (self.gladness}")
         print("Progress = {round(self.progress, 2)}")
    def live(self, day):

         day= "Day" + str(day) + "of" self.name + "life"
         print (f" (day: =^50}")
         live_cube random.randint(1, 3)
         if live cube as 1:
         self.to_study()
         elif live cube == 2:
         self.to_sleep()
         elif live cube == 3:
         self.to chill()
         self.end_of_day()
         self.is alive()

nick=Student (name="Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live (day)


