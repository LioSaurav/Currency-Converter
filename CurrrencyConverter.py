import requests

API_URL = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/"

# Currency symbols for better output formatting
CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "INR": "₹",
    "NPR": "Rs",
    "GBP": "£",
    "JPY": "¥",
    "AUD": "A$",
    "CAD": "C$",
    "CNY": "¥",
    "CHF": "CHF",
    "NZD": "NZ$",
}

def get_exchange_rates(base_currency):
    try:
        response = requests.get(API_URL + base_currency)
        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates']
        else:
            print("Error fetching data from the API. Please try again.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code. Please try again.")
        return None
    return amount * rates[to_currency] / rates[from_currency]

def manage_currencies():
    global CURRENCY_SYMBOLS
    while True:
        print("\nCurrency Management Menu:")
        print("1 - Add a Currency")
        print("2 - Update a Currency Symbol")
        print("3 - Delete a Currency")
        print("4 - View All Currencies")
        print("5 - Back to Main Menu")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            code = input("Enter the currency code (e.g., USD): ").upper()
            symbol = input("Enter the currency symbol (e.g., $): ")
            if code in CURRENCY_SYMBOLS:
                print(f"Currency {code} already exists.")
            else:
                CURRENCY_SYMBOLS[code] = symbol
                print(f"Currency {code} added with symbol '{symbol}'.")
        
        elif choice == "2":
            code = input("Enter the currency code to update: ").upper()
            if code in CURRENCY_SYMBOLS:
                symbol = input(f"Enter the new symbol for {code}: ")
                CURRENCY_SYMBOLS[code] = symbol
                print(f"Currency {code} updated to symbol '{symbol}'.")
            else:
                print(f"Currency {code} not found.")
        
        elif choice == "3":
            code = input("Enter the currency code to delete: ").upper()
            if code in CURRENCY_SYMBOLS:
                del CURRENCY_SYMBOLS[code]
                print(f"Currency {code} deleted.")
            else:
                print(f"Currency {code} not found.")
        
        elif choice == "4":
            print("\nCurrent Currencies:")
            for code, symbol in CURRENCY_SYMBOLS.items():
                print(f"{code}: {symbol}")
        
        elif choice == "5":
            print("Returning to the main menu.")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    print("---- Welcome to the Currency Converter ----")

    while True:
        print("\nMain Menu:")
        print("1 - Convert Currency")
        print("2 - Manage Currencies")
        print("3 - Exit")
        
        choice = input("Choose an option (1-3): ")

        if choice == "1":  # Currency Conversion
            base_currency = input("Enter your base currency (e.g., USD): ").upper()
            rates = get_exchange_rates(base_currency)
            if not rates:
                print("Unable to fetch exchange rates. Please try again.")
                continue

            print("\nAvailable Currencies:")
            for currency, symbol in CURRENCY_SYMBOLS.items():
                print(f"{currency} {symbol}")
            
            from_currency = input("\nEnter the currency you want to convert from: ").upper()
            to_currency = input("Enter the currency you want to convert to: ").upper()

            try:
                amount = float(input("Enter the amount to convert: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            converted_amount = convert_currency(amount, from_currency, to_currency, rates)
            if converted_amount is not None:
                from_symbol = CURRENCY_SYMBOLS.get(from_currency, "")
                to_symbol = CURRENCY_SYMBOLS.get(to_currency, "")
                print(
                    f"{amount} {from_currency} ({from_symbol}) = {converted_amount:.2f} {to_currency} ({to_symbol})"
                )

        elif choice == "2":  # Manage Currencies
            manage_currencies()

        elif choice == "3": # Exit
            print("Thank you for using the Currency Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
