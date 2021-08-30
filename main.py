from config import *


if __name__ == '__main__':

    print("Choose one of these options : ")
    print("  1 - Start")
    print("  2 - Exit")

    choice = int(input("Enter Options Num : "))

    if choice == 1:
        for key, value in symbols.items():
            print(f"  {value} - {key}")

        symbol_num = int(input("Enter Symbol Num : "))

        symbol = ""
        for key, value in symbols.items():
            if value == symbol_num:
                symbol = key

        if symbol != "":
            quantity = int(input("Enter Quantity : "))
            print(f'trade {quantity} - {symbol}')

        else:
            print("Wrong Symbol's Num")

    elif choice == 2:
        exit()

    else:
        print("Wrong Option's Num")
