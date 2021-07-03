import pickle

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return (f'{self.name} - {self.price}$')

    @staticmethod
    def sum(pr):
        sum = 0
        for i in pr:
            sum += i.price
        return sum

    @staticmethod
    def the_most_expensive(pr):
        expensive = pr[0].price
        for i in pr:
            print(type(expensive), type(i.price))
            if i.price > expensive:
                expensive = i
        return f'{expensive.name} - {expensive.price}$'


    @staticmethod
    def find(pr, find_name):
        for i in pr:
            if i.name == find_name:
                return f'{i.name} - {i.price}$'

        return 'the book haven`t this product'


book = []
b = True
while b:
    print('Menu: ')
    print('1 - Add product')
    print('2 - Show all products')
    print('3 - show general price')
    print('4 - show the most expensive product')
    print('5 - find product by name')
    print('0 - exit')
    n = int(input('Enter number: '))
    if n == 1:
        name = input('Enter name: ')
        price = int(input('Enter price: '))
        book.append(Product(name, price))
        with open('book.txt', 'wb') as file:
            pickle.dump(book, file)

    if n == 2:
        with open('book.txt', 'rb') as file:
            product = pickle.load(file)
        for i in product:
            print(i.show())

    if n == 3:
        with open('book.txt', 'rb') as file:
            product = pickle.load(file)
        print(Product.sum(product))

    if n == 4:
        with open('book.txt', 'rb') as file:
            product = pickle.load(file)
        print(Product.the_most_expensive(product))

    if n == 5:
        with open('book.txt', 'rb') as file:
            product = pickle.load(file)
        name = input('Enter name: ')
        print(Product.find(product, name))

    if n == 0:
        b = False

