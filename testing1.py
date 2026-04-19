def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("=" * 40)
    print("   Temperature Converter")
    print("=" * 40)
    
    choice = input("\nConvert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius? ")
    
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    else:
        print("Invalid choice!")
    
    print("=" * 40)

if __name__ == "__main__":
    main()