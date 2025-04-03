def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # No discount applied if less than 20%

while True:
    try:
        # Prompt user for input
        original_price = float(input("Enter the original price of the item: "))
        if original_price < 0:
            raise ValueError("Price cannot be negative.")
        
        discount_percentage = float(input("Enter the discount percentage: "))
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the result
        print(f"Final Price: ${final_price:.2f}")
        break  # Exit loop if inputs are valid

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
