class Employee:
    def __init__(self, name, id, email, phone, address) -> None:
        self.name = name
        self.id = id 
        self.Contact = self.Contact(email, phone, address)

    def show(self):
        print(self.name, self.id, end = ' ')
        self.Contact.show()

    class Contact():
        def __init__(self, email, phone, address) -> None:
            self.email = email
            self.phone = phone
            self.address = address

        def show(self):
            print(self.email, self.phone, self.address)


e1 = Employee('Keshav', 'RA2011003030106', 'keshav.banka2003@gmail.com', 8004775978, 'BBK - 225409')
e1.show()
