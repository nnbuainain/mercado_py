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

def register_product(product_list: list) -> bool:
    name = input('Enter the product name: ')

    if name == '':
        print('\n ########## Enter a valid name ##########')
        register_product(product_list)
    
    else:
        while True:
            try:
                price = float(input('Enter the product value: '))

            except ValueError:
                print('\n########## The value must be a number ##########')
            
            else:    
                new_product = Product(name, price)
                    
                product_list.append(new_product)
                
                print(f'\n########## The product: {new_product.name} was registered successfully ########## ')
                break    

def list_products(product_list: list) -> bool:
    print('\n ########## List of products ##########')
    
    for product in product_list:
        print(f'Code: {product.code}\t Name: {product.name}\t Price: {product.price}')
        