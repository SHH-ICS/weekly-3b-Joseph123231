#this program is very inefficient and i know that but by the time i was done i needed to start on php/html 
# Sorry it's such a long program that does not need to be long
# I spent too much time perfecting this that i ran out of time to make a simple version 
import math
lGtopping1tax = (1.00 + 6.00 )
lg1tax = (0.91)
LGtopping2tax = (1.75 + 6.00)
lg2tax = (1.01)
LGtopping3tax = (2.50 + 6.00 )
lg3tax = (1.11)
LGtopping4tax = (3.35 + 6.00)
lg4tax = (1.22)

XLtopping1tax = (11.00)
xltax1 = (1.43)
XLtopping2tax = (11.75 )
xltax2 = (1.53)
XLtopping3tax = (12.50)
xltax3 = (1.63)
XLtopping4tax = (13.35)
xltax4 = (1.74)
print("\nWelcome to pythonHut! \n")
pizza_yn = str(input("Do you want to order a pizza: ")) 
while True:
    if pizza_yn.lower() == "yes":
        print("\nGreat let's get started! ")
    else:
         print("\n ORDER TERMINATED\n")
         break
    
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
                    break


    elif size.lower() ==  'large' and num_toppings == '2':
         print(f"\nSubtotal: ${LGtopping2tax:.2f} ")
         print(f"Tax: ${lg2tax:.2f}")
         print(f"Total: ${lg2tax + LGtopping2tax:.2f}")

         again = input("\nWould you like to order another pizza? ")
         if again == 'yes':
                continue
         else: 
            print("Hope you enjoy your pizza! ")
            break
           
    elif size.lower() == 'large' and num_toppings == '3':
             print(f"\nSubtotal: ${LGtopping3tax:.2f} ")
             print(f"Tax: ${lg3tax:.2f}")
             print(f"Total: ${lg3tax + LGtopping3tax:.2f}")
             again = input("\nWould you like to order another pizza? ")
             if again == 'yes':
                continue
             else:
                print("Hope you enjoy your pizza! ") 
                break
    elif size.lower() ==  'large' and num_toppings == '4':
            print(f"\nSubtotal: ${LGtopping4tax:.2f} ")
            print(f"Tax: ${lg4tax:.2f}")
            print(f"Total: ${lg4tax + LGtopping4tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again.lower() == 'yes':
                continue
            else: 
                print("Hope you enjoy your pizza! ")
                break
            

#XL
    elif size.upper() == 'XL' and num_toppings == '1':
            print(f"\nSubtotal: ${XLtopping1tax:.2f} ")
            print(f"Tax: ${xltax1:.2f}")
            print(f"Total: ${xltax1 + XLtopping1tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again.lower() == 'yes':
                continue
            else:
                print("Hope you enjoy your pizza! ") 
                break
            
    elif size.upper() == 'XL' and num_toppings == '2':
            print(f"\nSubtotal: ${XLtopping2tax:.2f} ")
            print(f"Tax: ${xltax2:.2f}")
            print(f"Total: ${xltax2 + XLtopping2tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again.lower() == 'yes':
                continue
            else:
                print("Hope you enjoy your pizza! ")
                break
    elif size.upper() == 'XL' and num_toppings == '3':
            print(f"\nSubtotal: ${XLtopping3tax:.2f} ")
            print(f"Tax: ${xltax3:.2f}")
            print(f"Total: ${xltax3 + XLtopping3tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again.lower() == 'yes':
                continue
            else:
                print("Hope you enjoy your pizza! ")
                break
            
    elif size.upper() == 'XL' and num_toppings == '4':
            print(f"\nSubtotal: ${XLtopping4tax:.2f} ")
            print(f"Tax: ${xltax4:.2f}")
            print(f"Total: ${xltax4 + XLtopping4tax:.2f}")
            again = input("\nWould you like to order another pizza? ")
            if again.lower() == 'yes':
                continue
            else:
                print("Hope you enjoy your pizza! ")
                break