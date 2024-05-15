class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if not self.ingredients or not self.toppings:
            return []
        combinations = list()
        for ingredient in self.ingredients:
            for topping in self.toppings:
                combinations.append([ingredient, topping])
        return combinations


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
