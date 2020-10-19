# defining our celcius to fahrenheit calculator
def cel_to_fahr(temp):
    temp_in_fahr = ((9/5 * temp) + 32)
    return temp_in_fahr
    
# defining our celcius to fahrenheit calculator
def fahr_to_cel(temp):
    temp_in_cel = ((5/9 * temp) - 32)
    return temp_in_cel
    
try:
    def user_interaction():
        print("Press ---\n\t\t","1 for converting temp from celcius to fahrenheit.\n\t\t","2 for converting temp from fahrenheit to celcius.")
        user_choice = int(input("Enter any key mentioned above: \n"))
        
        if user_choice == 1:
            temp = float(input("Enter Your Temperature in celcius: \n"))
            print(f"The Temperature in fahrenheit is {round(cel_to_fahr(temp), 1)}.")
            
        elif user_choice == 2:
            temp = float(input("Enter Your Temperature in fahrenheit: \n"))
            print(f"The Temperature in celcius is {round(fahr_to_cel(temp), 1)}.")
        
        else:
            print("Please enter valid key.")
        
        print("Press--\n\t\t","r for again calculating the temp.\n\t\t","q for quit this temp calculator.")
        user_wish = input("Enter any key mentioned above: \n")
        
        if user_wish == 'r' or user_wish == 'R':
            user_interaction()
        
        elif user_wish == 'q' or user_wish == 'Q':
            print('Thanks for using Temperature Calculator.')
        
        else:
            print("Please enter valid key.")            

except Exception as E:
    print(f"\nE\n")

# calling up our main function
if __name__ == '__main__':
    user_interaction()
