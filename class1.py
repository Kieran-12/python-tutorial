class Things:
    pass
class Inanimate(Things):
    def build_in_street(self):
        print("stop")
class Sidewalks(Inanimate):
    pass
class Animate(Things):
    pass
class Animals(Animate):
    def breathes(self):
        print("breathing")
    def move(self):
        print("moving")
    def eat_food(self):
        print("eating food")
class Mammals(Animals):
    def feed_young_with_milk(self):
        print("feeding young")
class Giraffe(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def eat_leaves_from_trees(self):
        print("eating leaves")
    def find_food(self):
        
        self.move()
        print("I've found food!")
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()


reginald = Giraffe(1)
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffe(2)
harold.eat_leaves_from_trees()

reginald.find_food()

ozwald = Giraffe(100)
gertrude = Giraffe(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
