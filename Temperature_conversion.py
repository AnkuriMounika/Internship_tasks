# Temperature conversion functions

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Simple text-based UI to interact with the user
def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    
    choice = int(input("Choose a conversion option (1/2/3): "))
    temp = float(input("Enter the temperature value: "))
    
    if choice == 1:
        print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit")
        print(f"{temp} Celsius is {celsius_to_kelvin(temp)} Kelvin")
    elif choice == 2:
        print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius")
        print(f"{temp} Fahrenheit is {fahrenheit_to_kelvin(temp)} Kelvin")
    elif choice == 3:
        print(f"{temp} Kelvin is {kelvin_to_celsius(temp)} Celsius")
        print(f"{temp} Kelvin is {kelvin_to_fahrenheit(temp)} Fahrenheit")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
