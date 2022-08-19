class Cart():
    
    def __init__(self, cart_products: list):
        self.__cart_products = cart_products
        self.__total = 0
    
    @property
    def cart_products(self):
        return self.__cart_products    

    @property
    def total(self):
        self.__total = 0
        
        for product in self.__cart_products:
            self.__total += product['total_price']
        
        return self.__total

    def show_cart(self) -> bool:
        print('\n ########## List of products in the cart ##########')
        
        if len(self.__cart_products) != 0:
            
            for product in self.__cart_products:
                print(f"Code: {product['code']} \t Name: {product['name']}\
                    \t Quantity: {product['quantity']} \t Unit Price: {product['unit_price']}\
                    \t Total Price: {product['total_price']}")
            
            print(f"\n Total in your cart: {self.total}")
            
        else:
            print('\n ########## There is no product in the cart yet ##########')
    

def add_product_to_cart(product_list: list, cart_list: list) -> Cart:
    try:
        code = int(input('\n Enter the code of the product you would like to buy:'))
    
    except ValueError:
        print('\n ########## Enter a valid code ##########')
        
        add_product_to_cart(product_list, cart_list)

    else:
        if code in [product.code for product in product_list]:
            while True:
                try:
                    product_quantity = int(input('\n Enter the quantity of the product you would like to buy: '))
                
                except ValueError:
                    print('\n ########## Enter a valid quantity ##########')
                
                else:
                    if product_quantity > 0:
                        new_product = [{'code' : product.code, 'name' : product.name, \
                                        'quantity' : product_quantity, 'unit_price' : product.price, \
                                        'total_price' : product.price * product_quantity} \
                                        for product in product_list if product.code == code][0]
                        
                        if new_product['code'] not in [product['code'] for product in cart_list]:
                            cart_list.append(new_product)
                            
                            cart = Cart(cart_list)
                            
                            print(f"\n {new_product['name']} (qtd: {new_product['quantity']}) was added to the cart successfully")
                        
                        else:
                            for product in cart_list:
                                if product['code'] == new_product['code']:
                                    
                                    product['quantity'] += new_product['quantity']
                                    
                                    product['total_price'] += new_product['total_price']
                                    
                                    cart = Cart(cart_list)
                                    
                                    print(f"\n {new_product['name']} (qtd: {new_product['quantity']}) was added to the cart successfully")      
                    
                    else:
                        print(f'########## Enter a valid quantity, the minimum is 1 ##########')
                
                return cart
        else:
            print('\n ########## Code not found in list of product ##########')

def __del__(self) -> bool:
    print('The cart was cleared successfully')