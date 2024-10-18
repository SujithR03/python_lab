def currency_converter(amount, currency): 
    rates = { 
        'USD_to_EUR': 0.85, 
        'EUR_to_USD': 1.18, 
        'USD_to_GBP': 0.75, 
        'GBP_to_USD': 1.33 
    } 
    rate = rates.get(currency)  # Removed 'None' and unnecessary 'if' condition
    if rate: 
        return amount * rate 
    else: 
        return "Invalid currency pair" 

# Example usage: 
print(currency_converter(100, 'USD_to_EUR'))  # Output: 85.0 
print(currency_converter(100, 'EUR_to_USD'))  # Output: 118.0 
print(currency_converter(100, 'USD_to_INR'))  # Output: Invalid currency pair
