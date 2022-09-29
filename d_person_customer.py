import d_person as dp

def main():
    name = 'John'
    address = '1234 Main Street'
    phone_number = '111-222-3333'
    customer_number = '1234'
    mailing_list = 'True'

person1 = dp.Person(name, address, phone_number)

customer1 = dp.Customer(name, address, phone_number)

person1.print_person()

print()
print()
print()

customer1.print_person()