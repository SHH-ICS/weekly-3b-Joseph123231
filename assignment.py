import math
lGtopping1tax = (1.00 + 6.00 )
lg1tax = (0.91)
LGtopping2tax = (1.75 + 6.00 + 1.01)
lg2tax = (1.01)
LGtopping3tax = (2.50 + 6.00 + 1.11)
lg3tax = (1.11)
LGtopping4tax = (3.35 + 6.00 + 1.22)
lg4tax = (1.22)

XLtopping1tax = (11.00 + 1.43)
XLtopping2tax = (11.75 + 1.53)
XLtopping3tax = (12.50 + 1.63)
XLtopping4tax = (13.35 + 1.74)
print("\nWelcome to pythonHut\n")
pizza_yn = str(input("Do you want a pizza: ")) 
while True:
    if pizza_yn.lower() == "yes":
        print("\nGreat let's get started! ")
    size = input("\nwhat size do you want your pizza to be, Large or XL: ")
    num_toppings = str(input("you can have anwhere from 1-4 toppings "))

    if size.lower() ==  'large' and num_toppings == '1':
         print(f"\nSubtotal: ${lGtopping1tax:.2f} ")
         print(f"Tax: ${lg1tax:.2f}")
         print(f"Total: ${lg1tax + lGtopping1tax:.2f}")
              
    
         again = input("\nWould you like to order another pizza? ")
         if again == 'yes':
                continue
         else: 
                   print("Hope you enjoy your pizza! ")
    elif size.lower() ==  'large' and num_toppings == '2':
             print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${LGtopping2tax:.2f}")
             again = input("\nWould you like to order another pizza? ")
             if again == 'yes':
                continue
             else: 
                   print("Hope you enjoy your pizza! ")
    elif size.lower() == 'large' and num_toppings == '3':
             print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${LGtopping3tax:.2f}")
             again = input("\nWould you like to order another pizza? ")
             if again == 'yes':
                continue
             else: 
                   print("Hope you enjoy your pizza! ")
    elif size.lower() ==  'large' and num_toppings == '4':
            print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${LGtopping4tax:.2F}")
            again = input("\nWould you like to order another pizza? ")
            if again == 'yes':
                continue
            else: 
                   print("Hope you enjoy your pizza! ")
            

#XL 
    elif size.upper() == 'XL' and num_toppings == '1':
             print(f"\nYou chose a {size} pizza with {num_toppings} topping and your total is ${XLtopping1tax:.2f}")
             again = input("\nWould you like to order another pizza? ")
             if again == 'yes':
                continue
             else: 
                   print("Hope you enjoy your pizza! ")
    elif size.upper() == 'XL' and num_toppings == '2':
             print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${XLtopping2tax:.2f}")
             again = input("\nWould you like to order another pizza? ")
             if again == 'yes':
                continue
             else: 
                   print("Hope you enjoy your pizza!")
    elif size.upper() == 'XL' and num_toppings == '3':
            print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${XLtopping3tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again == 'yes':
                continue
            else: 
                   print("Hope you enjoy your pizza! ")
    elif size.upper() == 'XL' and num_toppings == '4':
            print(f"\nYou chose a {size} pizza with {num_toppings} toppings and your total is ${XLtopping4tax:.2f}")
            again = input("\nWould you like to order another pizza? ")

    if again == 'yes':
          continue
   
    
    else:
        break