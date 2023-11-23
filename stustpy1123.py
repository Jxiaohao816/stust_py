class Employee:
    def __init__( self,emp_name,emp_id,emp_salary,emp_department,emp_worktime):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        self.emp_worktime = emp_worktime
        self.emp_salary = emp_salary
        #建立資料時直接計算總薪資
        self.emp_salary = int(self.calculate_emp_salary())
    #更換部門
    def assign_department(self,change_department):
        self.emp_department = change_department
    #計算薪資(加上加班費)**未滿50會扣薪水
    def calculate_emp_salary(self):
        return self.emp_salary + (self.emp_worktime - 50)*(self.emp_salary/50)

    def print_employee_details(self):
        print(f"{self.emp_name},{self.emp_id},{self.emp_salary},{self.emp_department}")

#建立資料(姓名,ID,薪資,部門,時數)
Adams = Employee("Adams","E7876",50000,"ACCOUNTING",75)
Jones = Employee("JONES", "E7499", 45000, "RESEARCH",80)
Martin = Employee("MARTIN", "E7900", 50000, "SALES",65)
Smith = Employee("SMITH", "E7698", 55000, "OPERATIONS",30)
#更改部門
Adams.assign_department("SALES")
Jones.assign_department("ACCOUNTING")
#輸出
Adams.print_employee_details()
Jones.print_employee_details()
Martin.print_employee_details()
Smith.print_employee_details()
