import random
import string
import json


# Function to load client data from file
def load_data():
    with open("bank_data.json", 'r') as file:
        global accounts, clients, client_accounts
        data = json.load(file)
        accounts = {int(key): value for key, value in data.get('accounts', {}).items()}
        clients = {int(key): value for key, value in data.get('clients', {}).items()}
        client_accounts = {int(key): value for key, value in data.get('client_accounts', {}).items()}
        return accounts, clients, client_accounts

# Function to save client data to file
def save_data():
    global accounts, clients, client_accounts
    data = {
        'accounts': accounts,
        'clients': clients,
        'client_accounts': client_accounts
    }
    with open("bank_data.json", 'w') as file:
        json.dump(data, file, indent=2)

# Function to generate a random PIN with letters and digits
def generate_pin(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Functions for bank agent
def add_client():
    global clients, accounts, client_accounts
    last_client_number = max(clients.keys())
    client_num = last_client_number + 1

    def generate_account_num():
        random_num = random.randint(0, 100)
        account_num = client_num * 100 + random_num
        return account_num

    account_num = generate_account_num()
    balance = 0
    pin = generate_pin()

    clients[client_num] = pin
    client_accounts[client_num] = account_num
    accounts[account_num] = balance


def remove_client(account_to_remove):
    global clients, accounts, client_accounts
    del accounts[account_to_remove]

    for key, value in client_accounts.items():
        if value == account_to_remove:
            client_to_delete = key
            break

    del clients[client_to_delete]
    del client_accounts[client_to_delete]


# Functions for clients
def display_balance(account_num):
    balance = accounts[account_num]
    return balance

def modify_pin(x):
    global clients, accounts, client_accounts
    new_pin = input("Enter your new PIN: ")
    clients[x] = new_pin

def withdraw(account_num, amount):
    global clients, accounts, client_accounts
    if accounts[account_num] >= amount > 0:
        accounts[account_num] -= amount
        print(f"{amount} was successfully withdrawn")
        print(f"Balance now is: {accounts[account_num]}")

    else:
        print("Insufficient balance")
        

def deposit(account_num, amount):
    global clients, accounts, client_accounts
    accounts[account_num] += amount
    print(f"{amount} was successfully deposited")
    print(f"Balance now is: {accounts[account_num]}")
        
