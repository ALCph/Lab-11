# 1.) Employee and Productionworker
# The superclass
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number
        # Setting
    def set_employee_name(self, employee_name):
        self.employee_name = employee_name
    def set_employee_number(self, employee_number):
        self.employee_number = employee_number
        # Getting
    def get_employee_name(self):
        return self.employee_name
    def get_employee_number(self):
        return self.employee_number
# The subclass
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, pay_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.shift_number = shift_number
        self.pay_rate = pay_rate
        # Setting
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate
        # Getting
    def get_shift_number(self):
        return self.shift_number
    def get_pay_rate(self):
        return self.pay_rate
    
# A function for getting user input
def main():
    employee_name = input("Enter the employee's name: ")
    employee_number = input("Enter the employee's number: ")
    shift_number = int(input("Enter the employee's shift (1 for day, 2 for night): "))
    pay_rate = float(input("Enter the employee's hourly pay rate: "))

    # A blank worker for the attributes
    sample_worker = ProductionWorker(employee_name, employee_number, shift_number, pay_rate)

    # Printing the output
    print(f"Name: {sample_worker.get_employee_name()}")
    print(f"Number: {sample_worker.get_employee_number()}")
    if shift_number == 1:
        print('Shift: Day Shift')
    else:
        print('Shift: Night Shift')
    print(f"Hourly Pay Rate: ${sample_worker.get_pay_rate():.2f}")

#calling the main function
main()
#===================================================

# 2.) ShiftSupervisor Class
# Using the established superclass from exercise #1
class ShiftSuper(Employee):
    def __init__(self, employee_name, employee_number, annual_pay, bonus):
        Employee.__init__(self, employee_name, employee_number)
        self.annual_pay = annual_pay
        self.bonus = bonus
    # Setting
    def set_annual_pay(self, annual_pay):
        self.annual_pay = annual_pay
    def set_bonus(self, bonus):
        self.bonus = bonus
    # Getting
    def get_annual_pay(self):
        return self.annual_pay
    def get_bonus(self):
        return self.bonus

# A reused function for getting user input
def main():
    employee_name = input("Enter the supervisor's name: ")
    employee_number = input("Enter the supervisor's number: ")
    annual_pay = float(input("Enter the supervisor's annual salary: "))
    bonus = float(input("Enter the supervisor's production bonus: "))

    # A blank supervisor for the attributes
    sample_sv = ShiftSuper(employee_name, employee_number, annual_pay, bonus)

    # Printing the output
    print(f"Name: {sample_sv.get_employee_name()}")
    print(f"Number: {sample_sv.get_employee_number()}")
    print(f"Annual Salary: ${sample_sv.get_annual_pay():,.2f}")
    print(f"Production bonus: ${sample_sv.get_bonus():.2f}")
#calling the main function
main()
#===================================================

# 3.) Person and Customer Classes

# The main Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    # Setting
    def set_name(self, name):
        self.name = name
    def set_address(self, address):
        self.address = address
    def set_phone(self, phone):
        self.phone = phone
    # Getting
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_phone(self):
        return self.phone

# The Customer Subclass
class Customer(Person):
    def __init__(self, name, address, phone, cusID, mail):
        Person.__init__(self, name, address, phone)
        self.cusID = cusID
        self.mail = mail
    # Setting
    def set_cusID(self, cusID):
        self.cusID = cusID
    def set_mail(self, mail):
        self.mail = mail
    # Getting
    def get_cusID(self):
        return self.cusID
    def get_mail(self):
        return self.mail

# A function for getting user input
def main():
    name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    phone = input("Enter the customer's telephone number: ")
    cusID = input("Enter the customer number: ")
    mail_input = input("Mailing list? (yes/no): ")

    # A blank customer for our attributes
    customer = Customer(name, address, phone, cusID, mail_input)

    # Printing the output
    print(f"Name: {customer.get_name()}")
    print(f"Address: {customer.get_address()}")
    print(f"Phone: {customer.get_phone()}")
    print(f"Customer Number: {customer.get_cusID()}")
    if mail_input.lower() == 'yes':
        print('Sign them up for mailing list')
    else:
        print('Do not sign them up for mailing list')
# Calling the main function
main()
