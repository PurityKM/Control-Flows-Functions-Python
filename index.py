def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        end_price = price - (price * (discount_percent / 100))
        return end_price
    else:
        
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
end_price = calculate_discount(original_price, discount_percent)

# Print the final price
if end_price < original_price:
    print(f"The final price after applying the discount is: ${end_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")
