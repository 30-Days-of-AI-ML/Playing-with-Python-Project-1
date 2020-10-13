try:
    # defining our multiple calculator function
    def multiples(num):
        print(f"The 10 Multiples of {num} are --->\n")
        for i in range(1,11):
            print(f"{num}x{i} = {num*i}")

    # defining our user_interact function
    def user_interact():
        # taking number as input from the user
        num = int(input("Enter your Number: \n"))
        multiples(num)
    
        print("\nPress--\n\t\t","r for again finding the multipels of any number.\n\t\t","q for quit.")
        user_choice = input("\nEnter any key Mentioned above: \n")
    
        if user_choice == 'r' or user_choice == 'R':
            user_interact()
        
        elif user_choice == 'q' or user_choice == 'Q':
            print("\nThanks for using our Program.")
        
        else:
            print("\nPlease enter valid key.")

        
except Exception as E:
    print("\nE\n")
 
# calling our main function
if __name__ == '__main__':
    user_interact()
