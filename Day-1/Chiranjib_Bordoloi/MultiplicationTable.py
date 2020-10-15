# Function to multiply number and give output
def multi_table(num):
    print("Multiplication Table of", num, "\n")
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)


# Taking input from USER
num = int(input("Enter a number: "))

# Calling multi_table function
multi_table(num)
