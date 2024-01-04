class DrinkStore:
    def __init__(self):
        pass

class Employee(DrinkStore):
    def __init__(self, name, experience, work_hours):
        self.name = name
        self.experience = experience
        self.work_hours = work_hours

    def get_name(self):
        return self.name

    def get_experience(self):
        return self.experience

    def get_work_hours(self):
        return self.work_hours

    def calculate_monthly_salary(self):
        return self.work_hours * 183

    def increase_work_hours(self, extra_hours):
        self.work_hours += extra_hours
        print(f"Work hours increased to {self.work_hours} hours!")

    def increase_experience(self):
        self.experience += 1
        print(f"Experience increased to {self.experience} years!")


class Drink(DrinkStore):
    pass

class ColdDrink(Drink):
    def __init__(self, drink_name, ice, sugar):
        self.drink_name = drink_name
        self.ice = ice
        self.sugar = sugar

class HotDrink(Drink):
    def __init__(self, drink_name, sugar):
        self.drink_name = drink_name
        self.sugar = sugar


# 使用例子：
employee = Employee("John Doe", 3, 160)#建立員工資訊
print("Name:", employee.get_name())
print("Experience:", employee.get_experience())
print("Work Hours:", employee.get_work_hours())

employee.increase_work_hours(20)#增加工時
employee.increase_experience()#增加年姿
print("Updated Work Hours:", employee.get_work_hours()) #增加後的工時、年資
print("Updated Experience:", employee.get_experience())

print("-----------------------------------------------------")

cold_drink = ColdDrink("Iced Tea", "Less Ice", "Medium Sugar")
print("Cold Drink Name:", cold_drink.drink_name) #冷飲資訊
print("Ice Level:", cold_drink.ice)
print("Sugar Level:", cold_drink.sugar)
milk_tea = ColdDrink("Milktea","Less Ice", "Medium Sugar")
print("Cold Drink Name:", milk_tea.drink_name) #冷飲資訊
print("Ice Level:", cold_drink.ice)
print("Sugar Level:", cold_drink.sugar)
hot_drink = HotDrink("Coffe","No Suger")
print("Hot_Drink_Name:",hot_drink.drink_name)#熱飲資訊
print("Sugar Level:", hot_drink.sugar)
