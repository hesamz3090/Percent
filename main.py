import random

from config import *
from binance import Client

if __name__ == '__main__':

    print("Choose one of these options : ")
    print("  1 - Start")
    print("  2 - Exit")

    choice = int(input("Enter Options Num : "))

    if choice == 1:
        if profile["key_one"] != "" \
                and profile["secret_one"] != "" \
                and profile["key_two"] != "" \
                and profile["secret_two"] != "":
            for key, value in symbols.items():
                print(f"  {value} - {key}")

            symbol_num = int(input("Enter Symbol Num : "))

            symbol = ""
            for key, value in symbols.items():
                if value == symbol_num:
                    symbol = key

            if symbol != "":
                quantity = int(input("Enter Quantity : "))

                client_one = Client(profile.binance_api_key, profile.binance_api_secret)
                client_two = Client(profile.binance_api_key, profile.binance_api_secret)

                num = random.randint(1, 2)

                if num == 1:
                    side = "BUY"
                    un_side = "SELL"

                else:
                    side = "SELL"
                    un_side = "BUY"

                result_one = client_one.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity,
                )

                result_two = client_two.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity,
                )

                trailing_one = client_one.futures_create_order(
                    symbol=symbol,
                    type='TRAILING_STOP_MARKET',
                    side=un_side,
                    callbackRate=5
                )

                trailing_two = client_two.futures_create_order(
                    symbol=symbol,
                    type='TRAILING_STOP_MARKET',
                    side=un_side,
                    callbackRate=5
                )

            else:
                print("Wrong Symbol's Num")
        else:
            print("Please Edit Config.py")

    elif choice == 2:
        exit()

    else:
        print("Wrong Option's Num")
