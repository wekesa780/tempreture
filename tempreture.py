# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/8) * (fahrenheit - 32)
    return celsius

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Prompt the user to enter the temperature to be converted
temperature = input("Enter the temperature to be converted (e.g. 60°C or 45°F): ")

# Check if the temperature is in Celsius or Fahrenheit
if temperature.endswith("C"):
    celsius = float(temperature[:-2])
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit} in Fahrenheit")
elif temperature.endswith("F"):
    fahrenheit = float(temperature[:-2])
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius} in Celsius")
else:
    print("Invalid input. Please enter a temperature in the format 'XX°C' or 'XX°F'.")