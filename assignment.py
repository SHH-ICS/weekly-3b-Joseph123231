#these comments are things ive learned in the process of doing this project and could be useful for RST
# Note :.2f displays the number 2 digits after decimal instad of a big decimal number very useful for money calculations
# Note you can assign values to items in a list so long as you know what the potential input might be in my case its "Large" or "Extra Large"
# then it takes the string the user has typed and ascociates it the the value in my case 6.00 or 10.00 
#kinda like a reverse if statement the way i think of it 

# if user inputs large and 2 toppings it calls large from the list and it's value of 6.00 and it calls 2 for the list topping_costs and it's value of 1.75 and uses that to calculate subtotal
#so the names Large and XL represent to numerical value 
while True :   

    pizza_costs = {"Large": 6.00, "XL": 10.00}
    topping_costs = {"1": 1.00, "2": 1.75, "3": 2.50, "4": 3.35}
    HST = 0.13
    pizza_size = input("Enter pizza size (Large or XL): ")
    toppings = str(input("Enter number of toppings (1-4): "))
    subtotal = pizza_costs[pizza_size] + topping_costs[toppings]
    tax = subtotal * HST
    total = subtotal + tax

    print(f"\nYou ordered a {pizza_size} pizza with {toppings} toppings so your ...\n ")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    again = str(input("Do you wish to order another pizza? "))
    if again == "yes":
        continue
    else: 
        print("\nEnjoy your pizza!! \n")
        break
