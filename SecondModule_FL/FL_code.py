

class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee
    def get_info(self):
        if self.on_vacation == True:
            vacation_consistance = 'В отпуске'
        else:
            vacation_consistance = 'Работает'
        return f'У {self.name} зарплата в месяц {self.salary}. {vacation_consistance}'
        

inf_Employee = [
    Employee('Danil', 200000, True, True),
    Employee('Irina', 2000000, True, True),
    Employee('Kirill', 900000, False, True),
    Employee('Gleb', 8000, True, False),
    Employee('Alex', 100000, True, True)
    ]

for i in inf_Employee:
    if i.is_good_employee == False:
        inf_Employee.remove(i)
for i in inf_Employee:
    print(Employee.get_info(i))

