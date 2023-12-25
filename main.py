from functions import *

accounts, clients, client_accounts = load_data()

x = input("Are you an 'agent' or a 'client' (Please type in lowercase): ")
print("Welcome")

while True:
    if x == 'agent':
        print("\nMenu:")
        print("1. Add a client")
        print("2. Remove a client")
        print("3. Exit")
        choice = int(input("Enter your choice (1, 2, or 3): "))

        if choice == 1 : #Add a client
            add_client()
            print("Client added successfuly")
            print("clients:", clients)
            print("accounts:", accounts)
            print("client_accounts:", client_accounts)

        elif choice == 2 : #Remove a client
            account_to_remove = int(input("Enter the account number you wish to remove: "))
            if account_to_remove in accounts :
                remove_client(account_to_remove)
                print("Client removed successfuly")
                print("clients:", clients)
                print("accounts:", accounts)
                print("client_accounts:", client_accounts)
            else :
                print("Invalid account number")

        elif choice == 3: #Exit
            print("Exiting the program...")
            save_data()
            break


    elif x == 'client':
        print("\nMenu:")
        print("1. Display balance")
        print("2. Modify PIN")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Exit")
        choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))


        if choice == 1 : #Display balance
            account_num = int(input("Enter your account number: "))
            if account_num in accounts :
                print("Balance:", display_balance(account_num))
            else :
                print("Invalid account number")

        elif choice == 2 : #Modify PIN
            account_num = int(input("Enter your account number: "))
            if account_num in accounts:
                for key, value in client_accounts.items():
                    if value == account_num:
                        x = key

                modify_pin(x)
                print("PIN modified successfuly")

            else:
                print("Invalid account number")

        elif choice == 3 : #Withdraw
            account_num = int(input("Enter your account number: "))
            if account_num in accounts :
                amount = float(input("Enter the amount to withdraw: "))
                withdraw(account_num, amount)
            else:
                print("Invalid account number")

        elif choice == 4 : #Deposit
            account_num = int(input("Enter your account number: "))
            if account_num in accounts :
                amount = float(input("Enter the amount to deposit: "))
                deposit(account_num, amount)
            else:
                print("Invalid account number")
            
        elif choice == 5 : #Exit
            print("Exiting the program...")
            save_data()
            break
    
