class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items):
        sum = 0
        for p in purchased_items:
            if p in self.items:
                sum += self.items[p]
        return sum

    def __repr__(self):
        return "{} menu available from {}pm to {}pm".format(self.name, self.start_time, self.end_time) 

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if (time >= menu.start_time and time <= menu.end_time):
                available_menus.append(menu)
        return available_menus

    def __repr__(self):
        return "The address of this franchise is {address}".format(address=self.address)
  
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

arep_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a’ Arepa", arep_menu, 10, 20)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepas = Business("Take a' Arepa", [arepas_place])

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(dinner.calculate_bill(["eggplant caponata", "mushroom ravioli (vegan)", "espresso"]))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

basta_bazoo = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
print(arepas.franchises[0].menus[0])