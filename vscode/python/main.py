from math import prod
from re import I
import sys
class Item:
    def __init__ (self,strings):
        self.name =  strings[1]
        self.quantity = int(strings[2])
        self.cost = float(strings[3][1:])
    def getTotalCost(self):
        return self.cost * self.quantity
    def toString(self):
        return f"{self.name} x{self.quantity} = ${self.getTotalCost():.2f}"
    @staticmethod
    def parseItem(line):
        strings = line.split()
        if(strings[0] == "Grain"):
            return Grain(strings)
        else:
            return Produce(strings)
        

class Produce (Item):
    def __init__(self, strings):
        super().__init__(strings) 
        self.color = strings[4]
    def toString(self):
        return self.color + " "+super().toString()

class Grain(Item):
    def __init__(self, strings):
        super().__init__(strings) 
        self.weight = float(strings[4])
    def toString(self):
        return f"{self.weight:.2f} lb "+super().toString()

def main():
    if len(sys.argv) < 2:
        return 1
    with open(sys.argv[1]) as file:
        lines = file.readlines()
    items = []
    produce = []
    grains = []
    for line in lines:
        item = Item.parseItem(line)
        items.append(item)
        if isinstance(item,Grain):
            grains.append(item)
        else:
            produce.append(item)
    
    with open("output.txt","w") as file:
        file.write("All Items:\n")
        cost = 0.0
        for item in items:
            file.write(item.toString()+"\n")
            cost += item.getTotalCost()
        file.write(f"Total ${cost:.2f}\n\n")

        file.write("Grains:\n")
        cost = 0.0
        for item in grains:
            file.write(item.toString()+"\n")
            cost += item.getTotalCost()
        file.write(f"Total ${cost:.2f}\n\n")

        file.write("Produce:\n")
        cost = 0.0
        for item in produce:
            file.write(item.toString()+"\n")
            cost *= item.getTotalCost()
        file.write(f"Total ${cost:.2f}\n\n")
        



if __name__ == "__main__":
    main()