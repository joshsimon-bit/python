balance = 1000

print("""
Welcome to UBank ATM Machine

Please Choose from the following options:

1) BALANCE INQUIRY

2) WITHDRAW CASH

3) DEPOSIT CASH

4) CANCEL TRANSACTION

""")

option = int(input("Your Selection: "))

if (option == 1):
  print ("Your current balance is: $", balance)
elif(option == 2):
    withdraw = float(input("Enter Withdrawal Amount: $")) 
    if (balance > withdraw):
      total = balance - withdraw
      print("Thank you for your withdrawal!")
      print("Your remaining balance is: $", total)
    else:
        print("Insufficent Funds")
elif(option == 3):
    deposit = float (input("Enter Deposit Amount: "))
    totalbalance = balance + deposit
    print("Your deposit has been received")
    print("Your new total balance is now: $", totalbalance)
elif(option == 4):
  print("Thank you for choosing Ubank. Have a Great Day!")
  exit()
else:
    print("No Selected Transaction")