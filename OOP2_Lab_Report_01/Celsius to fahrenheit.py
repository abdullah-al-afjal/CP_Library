#define Function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#User input
celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} deg Celsius is equal to {fahrenheit} deg Fahrenheit")
