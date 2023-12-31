class Chicken:
    def __init__(self, name, cut, spice_level, is_roast, is_crispy):
        self.name = name
        self.cut = cut
        self.spice_level = spice_level
        self.is_roast = is_roast
        self.is_crispy = is_crispy
        self.order_quantity = 0
    
    def place_order(self, quantity):
        self.order_quantity += quantity
        print(f"{self.name}: {quantity} pieces ordered!")

    def add_spice(self, spice):
        self.spice_level += spice
        print(f"{self.name} spice level increased to {self.spice_level}!")

    def make_cut(self):
        self.cut= False
        print(f"{self.name} 老闆我的雞排不准切!!!")

    def display_info(self):
        print(f"品項: {self.name}, 要不要切: {self.cut}, 辣度: {self.spice_level}, Fried: {self.is_roast}, Crispy: {self.is_crispy}, Ordered Quantity: {self.order_quantity}")

# 建立四個炸雞物件
chicken1 = Chicken("Spicy", False, 5, False, False)
chicken2 = Chicken("Mild",True, 3, False, False)
chicken3 = Chicken("Super Spicy", True, 7, False, False)
chicken4 = Chicken("Extra Crispy", False, 6, False, False)

# 分別呼叫四個副程式，這裡可以看成奧客改單
chicken1.place_order(10)    #數量
chicken1.add_spice(2)   #另外加辣
chicken1.make_cut()  #叫老闆不要切
chicken1.display_info()  #顯示餐點資訊

print("--------------------")

chicken2.place_order(5)
chicken2.add_spice(1)
chicken2.make_cut()
chicken2.display_info()

print("--------------------")

chicken3.place_order(15)
chicken3.add_spice(0)
chicken3.make_cut()
chicken3.display_info()

print("--------------------")

chicken4.place_order(8)
chicken4.add_spice(0)
chicken4.make_cut()
chicken4.display_info()
