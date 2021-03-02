class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
        else:
            self.ingredients[ingredient] += quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if self.ingredients[ingredient] < quantity:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def make_order(self):
        PizzaDelivery.ordered = True
        ingredients = []
        for ingredient, quantity in self.ingredients.items():
            ingredients.append(f'{ingredient}: {quantity}')
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(ingredients)} and the price will be {self.price}lv.'

'''
Create a class called PizzaDelivery. 
Upon initialization it should receive name(string), price(float) and ingredients (dict). 
The class should also have an attribute ordered set to False by default. 
You should also create 3 instance methods:
-	add_extra(ingredient: str, quantity: int, ingredient_price: float):
o	if we already have this ingredient in our pizza increase the ingredient quantity with the given one and update the pizza price by adding the amount for the additional ingredients
o	if we don't have this ingredient in our pizza, we should add it and update the pizza price

-	remove_ingredient(ingredient: str, quantity: int, ingredient_price: float):
o	if we don't have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {name}!"
o	if we have the ingredient, but we try to remove more than we have available we should return the following message 
"Please check again the desired quantity of {ingredient}!", otherwise remove the given quantity of the ingredient and update the pizza price

-	make_order() - set the attribute ordered to True and return the following message 
"You've ordered pizza {name} prepared with {all ingredients and their quantities separated with coma and space} and the price will be {price}lv.". 
Please have in mind that once the pizza is ordered no further changes are allowed. 
We should return the following message if the customer tries to change it: "Pizza {name} already prepared and we can't make any changes!"

'''
margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
