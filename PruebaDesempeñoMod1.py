# Prueba de desempeño módulo 1

import re


productList = [] # Declare an empty list.

def addProduct(name, price, amount): # Function to create dictionaries and add it's to the list.
    product = {
        "name" : name,
        "price": price,
        "amount": amount
    }
    productList.append(product)

# Here we create 5 products with the addProduct function.
addProduct("Mineral water", 3500, 50)
addProduct("Sparkling water", 3500, 50)
addProduct("Hatsu tea", 6500, 30)
addProduct("Cocacola", 6500, 40)
addProduct("Cocacola zero", 6500, 20)

def getData(): # Function to obtain product data.

    while True:
            productName = input("Please enter the product name:\n").strip()
            if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", productName):
                break
            else:
                print("The product name may contain letters and spaces without numbers or symbols.")

    while True:
        try:
            productPrice = float(input("Please enter the price product:"))
            if productPrice < 0:
                print("The product price cannot be less than 0")
                continue
            break
        except ValueError:
            print("Please enter a correct amount")
            break


    while True:
        try:
            amount = int(input("Please enter the quantity of the product"))
            if amount >= 0:
                print("Product added correctly\n")
                break
            else:
                print("The amount cannot be less than 0")

        except ValueError:
            print("The product amount must be an integer")

    addProduct(productName, productPrice, amount)


def consultProduct(searchProduct): # Function to search products in the list by name.
    for product in productList:
        if product["name"].lower() == searchProduct.lower():
            print(product)
            return product
    else:
        print("The product doesn't exist.")
        return None

def searchProduct(): # Function to obtain only the product name.
    while True:
        searchProduct = input("Please enter the product name to search:\n").strip()
        if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", searchProduct):
            return searchProduct
        else:
            print("The product name may contain letters and spaces without numbers or symbols.")

def getNewPrice():
    while True:
        try:
            newPrice = float(input("Please enter the new price of the product:"))
            if newPrice < 0:
                print("The product price cannot be less than 0")
            return newPrice
        except ValueError:
            print("Please enter a correct amount")

def updatePrice(name, newPrice):
    product = consultProduct(name)
    if product:
        product["price"] = newPrice
        print(f"Price updated! the new price of {product["name"]} is ${product["price"]} ")
    else:
        return



def deleteProduct(nameProductDelete):
    product = consultProduct(nameProductDelete)
    if product:
        option = (input(f"Desea eliminar {product["name"]}?: Yes/No \n")).lower()
        if option == "yes":
            productList.remove(product)
            print("Product deleted correctly\n")
        else:
            return


def calculateInventoryPrice(): # Function to calculate the total inventory value and print the value.
    totalInventoryValue = 0

    for product in productList:
        totalInventoryValue = product["price"] * product["amount"] + totalInventoryValue

    return totalInventoryValue






def menu(): # We create a menu with match case structure.
    while True:
        option = input("\nWelcome to FreeMarket! Please choose an option:\n"
                       "1: To add a new product\n"
                       "2: To search for a product in the inventory\n"
                       "3: To update an product price\n"
                       "4: To delete a product of the invetory\n"
                       "5: To calculate the inventory price\n"
                       "6: Exit\n")

        match option:
            case "1":
                getData()
            case "2":
                product = searchProduct()
                consultProduct(product)
            case "3":
                name = searchProduct()
                newPrices = getNewPrice()
                updatePrice(name, newPrices)
            case "4":
                nameDelete = searchProduct()
                deleteProduct(nameDelete)
            case "5":
                print(f"The total inventory value is ${calculateInventoryPrice()}")
            case "6":
                print("Thank you for your visit! Have a nice day.")
                break
            case _:
                print("Invalid option")

menu() # Call the menu() function to start the program.




