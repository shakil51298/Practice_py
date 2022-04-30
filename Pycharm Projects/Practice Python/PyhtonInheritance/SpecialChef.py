from ChefCommon import ChefCommon
# inheritance is here...
class SpecialChef(ChefCommon):
    # overriding make_fish
        # def make_fish(self):
        #     print("can make fish")
    def make_fish(self):
        print("he only can make salmon fish fry")

    def chinese_food(self):
        print("Can make chinese food")