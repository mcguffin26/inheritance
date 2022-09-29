class Person:

    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone Number:', self.__phone_number)

    def __init__(self, name, address, number, customer_number, mailing_list):

        Person.__init__(self, name, address, number)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def print_person(self):
        print('METHOD #1')
        print('Name:', Person.get_name(self))
        print('Address:', Person.get_address(self))
        print('Phone:', Person.get_number(self))

        print()
        print()

        print('METHOD #2')
        Person.print_person(self)

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list
    
    


