class Person:
    def __init__(self, name, address):
        self.set_name(name)
        self.set_address(address)


    def set_name(self, name):
        self.name=name

    def set_address(self, address):
        self.address=address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address


person1 = Person('IU', 'seoul')
person2 = Person('sana', 'osaka')

print(f'Nome: {person1.get_name()}, endereço: {person1.get_address()}')
print(f'Nome: {person2.get_name()}, endereço: {person2.get_address()}')