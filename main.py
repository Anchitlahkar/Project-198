import os

billno = 0
customer_in_line = True


def billing():
    customer_name = input("Name:\t")
    total = 0

    print("\nEnter Twice to Complete the bill\n")

    while True:

        cost = input("Cost:\t")

        if cost == "":
            return customer_name, total

        quantity = input("Quantity: \t")
        print("\n")

        if quantity == "":
            return customer_name, total

        total += float(quantity)*float(cost)


while customer_in_line:
    billno += 1
    
    while customer_in_line:
        try:
            customer, total = billing()
    
            os.system("CLS")
    
            print("_"*50)
            print(f"Bill no: {billno}")
            print(f"\nName: {customer}")
            print(f"\nTotal: ₹{total}")
            print("\n\n*******Thank You for shopping with us*******\n")
            print("_"*50)

            new = input("\n\nNew Customer y/n:\t")
    
            if new == "y" or new == "Y":
                os.system("CLS")
                break
        
            else:
                customer_in_line = False

        except:
            break
    
