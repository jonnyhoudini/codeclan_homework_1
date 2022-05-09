# WRITE YOUR FUNCTIONS HERE

    # def test_pet_shop_name(self):
    #     name = get_pet_shop_name(self.cc_pet_shop)
    #     self.assertEqual("Camelot of Pets", name)

def get_pet_shop_name(shop):
    return shop["name"]

    # def test_total_cash(self):
    #     sum = get_total_cash(self.cc_pet_shop)
    #     self.assertEqual(1000, sum)

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

    # def test_add_or_remove_cash__add(self):
    #     add_or_remove_cash(self.cc_pet_shop,10)
    #     cash = get_total_cash(self.cc_pet_shop)
    #     self.assertEqual(1010, cash)

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

    # def test_pets_sold(self):
    #     sold = get_pets_sold(self.cc_pet_shop)
    #     self.assertEqual(0, sold)

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

    # def test_increase_pets_sold(self):
    #     increase_pets_sold(self.cc_pet_shop,2)
    #     sold = get_pets_sold(self.cc_pet_shop)
    #     self.assertEqual(2, sold)

def increase_pets_sold(shop, num):
    shop["admin"]["pets_sold"] += num

        # def test_stock_count(self):
        # count = get_stock_count(self.cc_pet_shop)
        # self.assertEqual(6, count)

def get_stock_count(shop):
    return len(shop["pets"])

    # def test_all_pets_by_breed__found(self):
    #     pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
    #     self.assertEqual(2, len(pets))

def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(breed)
    return pets

    # def test_find_pet_by_name__returns_pet(self):
    #     pet = find_pet_by_name(self.cc_pet_shop, "Arthur")
    #     self.assertEqual("Arthur", pet["name"])

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

    # def test_remove_pet_by_name(self):
    #     remove_pet_by_name(self.cc_pet_shop, "Arthur")
    #     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")
    #     self.assertIsNone(pet)

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

    # def test_add_pet_to_stock(self):
    #     add_pet_to_stock(self.cc_pet_shop, self.new_pet)
    #     count = get_stock_count(self.cc_pet_shop)
    #     self.assertEqual(7, count)

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

# def test_customer_cash(self):
#     cash = get_customer_cash(self.customers[0])
#     self.assertEqual(1000, cash)

def get_customer_cash(customer):
    return customer["cash"]

# def test_remove_customer_cash(self):
#     customer = self.customers[0]
#     remove_customer_cash(customer, 100)
#     self.assertEqual(900, customer["cash"])

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

    # def test_customer_pet_count(self):
    #     count = get_customer_pet_count(self.customers[0])
    #     self.assertEqual(0, count)

def get_customer_pet_count(customer):
    return len(customer["pets"])

    # def test_add_pet_to_customer(self):
    #     customer = self.customers[0]
    #     add_pet_to_customer(customer, self.new_pet)
    #     self.assertEqual(1, get_customer_pet_count(customer))

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

    # def test_customer_can_afford_pet__sufficient_funds(self):
    #     customer = self.customers[0]
    #     can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
    #     self.assertEqual(True, can_buy_pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False


# def test_sell_pet_to_customer__pet_found(self):
#         customer = self.customers[0]
#         pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

#         sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#         self.assertEqual(1, get_customer_pet_count(customer))
#         self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
#         self.assertEqual(100, get_customer_cash(customer))
#         self.assertEqual(1900, get_total_cash(self.cc_pet_shop))


def sell_pet_to_customer(shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet) == True:
        #remove the pet from the shop
        remove_pet_by_name(shop, pet)
        #add the cash to the shop
        add_or_remove_cash(shop, pet["price"])
        #increase pets sold
        increase_pets_sold(shop, 1)
        #add the pet to the customer
        add_pet_to_customer(customer, pet)
        #remove the cash from the customer
        remove_customer_cash(customer, pet["price"])




    # def test_sell_pet_to_customer__pet_not_found(self):
    #     customer = self.customers[0]
    #     pet = find_pet_by_name(self.cc_pet_shop,"Dave")

    #     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    #     self.assertEqual(0, get_customer_pet_count(customer))
    #     self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
    #     self.assertEqual(1000, get_customer_cash(customer))
    #     self.assertEqual(1000, get_total_cash(self.cc_pet_shop))
