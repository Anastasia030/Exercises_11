from task_2 import Cart, Product


def menu():
    data_product = []
    action = 0
    while action != 7:
        action = int(input('Select the action you want to perform: \n'
                           '1. Download product data from a file.\n'
                           '2. Add an item to the cart.\n'
                           '3. Remove the product from the shopping cart.\n'
                           '4. View the contents of the shopping cart.\n'
                           '5. Make an order.\n'
                           '6. Clear cart.\n'
                           '7. Complete.\n'
                           'Enter: '))
        print('----------------------------------------')

        with open('product.txt', 'r') as file_prdct:
            description = file_prdct.readline()
            for product in file_prdct:
                product = product.rstrip().split(';')
                prdct = Product(product[1])
                prdct.price = product[2]
                information = product[0] + ' ' + str(prdct)
                data_product.append(information)

        if action == 1:
            print('Product number |Product name |Country |Manufacturer |Price')
            for goods in data_product:
                print(goods)
                print('')

        if action == 2:
            choice = int(input('Select the product you want to add: '))
            Cart(data_product[choice - 1][3:])
            Cart.total_cost += int(data_product[choice - 1].split('/')[2][1:].rstrip())

        if action == 3:
            for number in range(len(Cart.all_cart)):
                print(number + 1, Cart.all_cart[number])
            choice = int(input('Select the product you want to delete: '))
            Cart.total_cost -= int(str(Cart.all_cart[choice - 1]).split('/')[2][1:].rstrip())
            Cart.all_cart.pop(choice - 1)

        if action == 4:
            for product in Cart.all_cart:
                print(product)
            Cart.write()

        if action == 5:
            Cart.write()

        if action == 6:
            Cart.all_cart.clear()

    with open('cart.txt', 'a') as file_prdct:
        Cart.counter()
        print(f'The total amount: {Cart.total_cost}', file=file_prdct)


menu()