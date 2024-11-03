def show_balance(balance):
    print(f'Your balance is $ {balance:.2f}')

def deposit(balance):
    amount = float(input('Enter amount to deposit: '))
    if amount > 0:
        balance += amount
        print(f'${amount} deposited successfully!')
    else:
        print('Invalid amount. Please enter a positive value.')
    return balance

def withdraw(balance):
    amount = float(input('Enter amount to withdraw: '))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f'${amount} withdrawn successfully!')
        else:
            print('Insufficient balance.')
    else:
        print('Invalid amount. Please enter a positive value.')
    return balance

def main():
    balance = 0  
    is_running = True

    while is_running:
        print('Banking Program')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)  
        elif choice == '3':
            balance = withdraw(balance)  
        elif choice == '4':
            is_running = False
            print('Exiting the program. Have a nice day!')
        else:
            print('That is not a valid choice.')

    print('Thank you, have a nice day!')


main()
         
  
        
    
