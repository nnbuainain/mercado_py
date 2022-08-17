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
                    new_product = [{'code':product.code, 'name': product.name} for product in product_list if product.code == code]
                    cart_list.append(new_product)
                    cart = Cart(cart_list)
                
                else:
                    print('\n ########## Invalid code ##########')
                
                
                
                #if code in [product.code for product in product_list]:
                #    for product in product_list:
                #        if code == product.code:
                #            p = product
                #            print(p)
                    
                    #quantity = int(input('\n Enter the quantity of the product you would like to buy: '))
                    #cart.append({product.code:quantity})
                    #print(cart)
                    #print(f'\n You added {quantity} {product.code} to your cart')
            
            else:
                print('\n ########## There is no registered product yet ##########')

        elif option == 6:
            print('\n ########## Thank you for using our E-Commerce ##########')
            break        

        else:
            print(f'\n ########## Invalid code, please type an option between 1 and 6 ##########')
        
    print(f'\nExiting the system...\n')

if __name__ == '__main__':
    main()
