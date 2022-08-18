class Product():
    code_generator = 0

    def __init__(self, name, price):
        self.__code = Product.code_generator + 1
        self.__name = name
        self.__price = float(round(price , 2))
        Product.code_generator = self.__code
    
    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

def register_product(product_list):
    name = input('Enter the product name: ')

    price = float(input('Enter the product value: '))

    new_product = Product(name, price)
        
    product_list.append(new_product)
    
    print(f'\nThe product: {new_product.name} was registered successfully')
    

def list_products(product_list):
    print('\n ########## List of products ##########')
    for product in product_list:
        print(f'Code: {product.code}\t Name: {product.name}\t Price: {product.price}')