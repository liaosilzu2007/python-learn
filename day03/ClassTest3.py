class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
cat = Cat()
cat.run()
print('=============================')
a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print('==============================')
print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print(type(b))
print("+++++++++++++++++++++++++++++++")


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return  self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

# print(getattr(obj, 'z'))
print(getattr(obj, 'z', 404))
