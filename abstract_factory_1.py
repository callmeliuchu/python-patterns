# -*- coding:utf8 -*


class Pet:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplemented


class Dog(Pet):

    def speak(self):
        print('wang wang wang')

    def __repr__(self):
        return f'Dog({self.name})'


class Cat(Pet):

    def speak(self):
        print('miao miao miao')

    def __repr__(self):
        return f'Cat({self.name})'


class PetShop:

    def __init__(self,pet_factory):
        self.pet_factory = pet_factory

    def get_pet(self,name):
        return self.pet_factory(name)

pet_shop = PetShop(Cat)
for name in 'lucy jack helen'.split(' '):
    pet = pet_shop.get_pet(name)
    print(pet)
    pet.speak()

