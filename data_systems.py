item_names = ["Apple", "Bread", "Milk", "Eggs"]

item_prices = [1.0, 2.50, 3.00, 4.50]

item_stock = [100, 20, 50, 4]

while(True):
    print()
    print("Choose Options")
    print("(A) View inventory")
    print("(B) Purchase item")
    print("(C) Restock item")
    print("(D) Exit")
    opt=input().upper()
    match opt:
        case 'A':
            print()
            print("Item name         Quantity       Price")
            for i in range(len(item_names)):
                print(" ",item_names[i],end="")
                for j in range(18-len(item_names[i])):
                    print("",end=" ")
                
                print(item_stock[i],end="")
                for j in range(13-len(str(item_stock[i]))):
                    print("",end=" ")
                
                print(f"{item_prices[i]}₹")
            print()
            for i in range(len(item_names)):
                if item_stock[i]<5:
                    print(f"!! {item_names[i]} is low in stock !!")
                print()
        case 'B':
            name=input("What item? ")
            quan=int(input("How much? "))
            if(item_stock[item_names.index(name)]>=quan):
                item_stock[item_names.index(name)]-=quan
                total=quan*item_prices[item_names.index(name)]
                print()
                print(f"Sir your total will be {total} ₹")
                print()
            else:
                print()
                print("Not enough stock, Sorry")
                print()
        case 'C':
            name=input("What item to restock? ")
            quan=int(input("By how much? "))
            item_stock[item_names.index(name)]+=quan
        case 'D':
            print()
            print("Thank you for using our service")
            print()
            break
        case _:
            print()
            print("Invalid option selected")
            print()