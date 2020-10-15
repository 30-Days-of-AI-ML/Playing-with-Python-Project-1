# Function to convert Celsius to Fahrenheit
def C_to_F():
    cel = float(input("Enter temperature in Celsius: "))
    fah = (cel * 9 / 5) + 32
    print(cel, "°C =", fah, "F")


# Function to convert Fahrenheit to Celsius
def F_to_C():
    fah = float(input("Enter temperature in fahrenheit: "))
    cel = (fah - 32) * 5 / 9
    print(fah, "F =", cel, "°C")


# Menu for selection
print("1. Celcius to Farenheit")
print("2. Farenheit to Celcius")

choice = int(input("Enter a Selection: "))

if (choice == 1):
    print("\nCelcius to Farenheit\n")
    C_to_F()
elif (choice == 2):
    print("\nFarenheit to Celcius\n")
    F_to_C()
else:
    print("Invalid Selection!!")
