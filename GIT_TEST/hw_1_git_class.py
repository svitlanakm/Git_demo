class Appliance:
    tech_class: 'Home_Appliance'
    def __init__(self, name, weight, color, feeding, do):
        self.name = name
        self.weight = weight
        self.color = color
        self.__feeding = feeding
        self.do = do

    def print_info(self):
        return f'This {name} is for {do}ing'

appl = Appliance('robot_vacuum_cleaner', 5, 'black', 'electricity', 'clean')

print(appl.__dict__)
print(appl.__class__)




