from numpy import prod, product
from product import Product, register_product, list_products
from cart import Cart
import json

product_list = []
cart_list = []

def menu():
    print('\n ########## Welcome to my E-Commerce ##########')
    print(' ###### Select one of the options below #######')
    print('\n 1 - Register product')
    print('\n 2 - List products')
    print('\n 3 - Buy product')
    print('\n 4 - See Cart')
    print('\n 5 - Checkout')
    print('\n 6 - Exit')

def main():

    option = None
    
    while option != 6:
        menu()
        
        option = int(input('\n Enter the option: '))

        if option == 1:
            
            name, price = register_product()
            
            new_product = Product(name, price)
            
            product_list.append(new_product)
        
            print(f'\nThe product: {new_product.name} was registered successfully')

        elif option == 2:
                
            if len(product_list) != 0:

                print('\n ########## List of products ##########')
                
                list_products(product_list)

            else:
                print('\n ########## There is no product registered yet ##########')
        
        elif option == 3:
            if len(product_list) != 0:
                print('\n ########## List of products ##########')
                
                list_products(product_list)

                code = int(input('\n Enter the code of the product you would like to buy: '))

                if code in [product.code for product in product_list]:
                    product_quantity = int(input('\n Enter the quantity of the product you would like to buy: '))
                    
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
                    print('\n ########## Invalid code ##########')
        
        elif option == 4:
            if len(cart_list) != 0:
                print('\n ########## List of products in the cart ##########')
                
                cart.show_cart()
            
            else:
                print('\n ########## Your cart is currently empty ##########')

        elif option == 6:
            print('\n ########## Thank you for using our E-Commerce ##########')
            break        

        else:
            print(f'\n ########## Invalid code, please type an option between 1 and 6 ##########')
        
    print(f'\nExiting the system...\n')

if __name__ == '__main__':
    main()
