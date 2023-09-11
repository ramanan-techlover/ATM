from cardHolder import cardHolder

def print_menu():
    #  Print options to user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much Money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your Money. Your new balance is: ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much Money would you like to withdraw: "))
        #  Check if user has enough money
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You are good to go! Thank you :)")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ",cardHolder.get_balance())

if __name__=="__main__":
    current_user = cardHolder("","","","","")
    list_of_cardHolders =[]
    list_of_cardHolders.append(cardHolder("4532611266538787", 1234, "Ramanan", "R", 3233.53))
    list_of_cardHolders.append(cardHolder("4532027608511534", 4321, "Suki", "S", 3053.32))
    list_of_cardHolders.append(cardHolder("4532305939580575", 9999, "Monish", "Kumar", 2345.98))
    list_of_cardHolders.append(cardHolder("4532784864683507", 2468, "Pugal", "Arasan", 1567.64))
    list_of_cardHolders.append(cardHolder("4532637965006706", 4826, "Arul", "Kumar", 2890.12))

    #  Prompt user for debit card number
    debitcardNum = ""
    while True:
        try:
            debitcardNum = input("Please insert your debit card: ")
            #  check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitcardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")

#  Prompt for PIN
while True:
    try:
        userPin = int(input("Please enter your pin: ").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN. Please try again.")
    except:
        print("Invalid PIN. Please try again.")

#  Print options
print("Welcome ", current_user.get_firstname(),":)")
option = 0
while (True):
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid input. Please try again.")

    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        check_balance(current_user)
    elif(option == 4):
        break
    else:
        option = 0
print("Thank you. Have a nice day :)")