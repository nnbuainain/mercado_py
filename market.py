from numpy import prod, product
from product import Product, register_product, list_products
from cart import Cart, add_product_to_cart

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

def checkout(cart, cart_list):
    print(f'\n The total amount to be paid is: {cart.total}')

    print(f'\n Purchase successfully completed')

    del cart

    cart_list.clear()

def main():
    option = None
    
    while option != 6:
        menu()
        
        try:
            option = int(input('\n Enter the option: '))
        
        except ValueError:
            print('\n########## Enter a valid option ########## ')
        
        else:
            if option == 1:
                register_product(product_list)

            elif option == 2: 
                if len(product_list) != 0:
                    list_products(product_list)

                else:
                    print('\n ########## There is no product registered yet ##########')
            
            elif option == 3:
                if len(product_list) > 0:
                    list_products(product_list)
                    
                    cart = add_product_to_cart(product_list, cart_list)
                
                else:
                    print('\n ########## There are no products available to be bought ##########')
                    print('\n ########## Register a new product first ##########')

            elif option == 4:
                if len(cart_list) > 0:
                    
                    cart.show_cart()

                else:
                    print('\n ########## Your cart is currently empty ##########')
            
            elif option == 5:
                print('\n ########## Checkout ##########')
                
                if len(cart_list) > 0:
                    checkout(cart, cart_list)
                
                else:
                    print('\n ########## Your cart is currently empty ##########')

            elif option == 6:
                print('\n ########## Thank you for using our E-Commerce ##########')
                break        

            else:
                print(f'\n ########## Please type an option between 1 and 6 ##########')
        
    print(f'\nExiting the system...\n')

if __name__ == '__main__':
    main()