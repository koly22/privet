class Mother:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character  = "good"
        self. eyecolor = "brown"

class Father:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.money = "4k"
class Son(Mother, Father):
    def print_info(self):
        print(self.character)
       # print(self.eyecolor)
        print(self.money)

Kolya = Son(model ="Kolya")
Kolya.print_info()


