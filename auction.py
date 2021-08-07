#from replit import clear
#HINT: You can call clear() to clear the output in the console.
# from art import logo
#print(f"{logo}\n Welcome to the secret auction program.")
ledger = {}
again = True

def auctioneer (again): 
  winning_bid = 0
  winner = ""
  while again:
    nama = input("What is your name? ")
    amount = int(input("How much are you bidding? $"))
    ledger[nama] = amount
    if input("Are there any more bidders? yes/no \n") == "yes":
      #clear()
      continue
    else:
      for key in ledger:
        if ledger[key] > winning_bid:
          winning_bid = ledger[key]
          winner = key
        else:
          continue
      print (f"The winner is {winner}.")
      again = False

auctioneer(again)