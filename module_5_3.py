class House:
    def __init__(self,name, number_of_floors ):
        self.name = name                          # номер этажа
        self.number_of_floors = number_of_floors

    def __str__(self):
            return f"Название: {self.name}, Количество этажей: {self.number_of_floors}"

    def go_to(self, new_floor):  # на который нужно приехать.
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует")
                break

    def __len__(self):
        return  self.number_of_floors
# __eq__
    def __eq__(self, other):
            return self.number_of_floors == other.number_of_floors

#__lt__
    def __lt__(self, other):
            return self.number_of_floors < other.number_of_floors

# __le__
    def __le__(self, other):
            return self.number_of_floors <= other.number_of_floors
#__gt__
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
#__ge__
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
#__ne__
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
#__add__
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
#__radd__
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


h1 = House('ЖК Elbrus', 10)
h2 = House('ЖК Akathia', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
