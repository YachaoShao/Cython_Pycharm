class robot:
    population = 0
    def __init__(self,name):
        self.name = name
        print("Initializing {}".format(self.name))
        robot.population +=1

    def die(self):
        print("{} is being destroyed".format(self.name))
        robot.population -=1

        if robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(self.population))

    def say_hi(self):
        print("Greetings, my master call me {}".format(self.name))

robo1 = robot("T1")
robo1.say_hi()

robo2 = robot("T2")
robo2.say_hi()

robo1.die()

