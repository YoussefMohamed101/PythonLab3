from Employee import Employee
class Office:
    employeesNum = 0
    def __init__(self,name,Employees):
        self.name = name
        self.Employees = Employees

    def get_All_employees(self):
        emps = []
        for emp in self.Employees:
            emps.append(emp)
        return emps


    def get_employee(self,id):
        for emp in self.Employees:
            if emp.id == id:
                return emp

    def hire(self,emp):
        self.Employees.append(emp)
        Office.employeesNum  += 1

    def fire(self,id):
        for emp in self.Employees:
            if emp.id == id:
                self.Employees.remove(emp)
                Office.employeesNum  -= 1

    def deduct(self,id,deduction):
        for emp in self.Employees:
            if emp.id == id:
                emp.salary -= deduction

    def reward(self,id,rewards):
        for emp in self.Employees:
            if emp.id == id:
                emp.salary += rewards

    def check_lateness(self, empld, moveHour):
        for employee in self.employees:
            if employee.id == empld:
                if moveHour > 9:
                    employee.salary -= 10
                else:
                    employee.salary += 10

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time = distance / velocity
        if moveHour + time > targetHour:
            return True
        else:
            return False


    @classmethod
    def change_emps_num(cls,num):
        cls.employeesNum = num
