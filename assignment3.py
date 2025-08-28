def calculate_discount(price, discount_percent):
    """
    Returns price after applying discount if discount_percent >= 20%.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

def main():
    try:
        # Get user inputs
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Display the result
        if discount_percent >= 20:
            print(f"Discount applied! Final price is: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price remains: {price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percent.")

if __name__ == "__main__":
    main()
