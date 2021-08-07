import random
#from art import logo
#from replit import clear
#def #screen_wipe():
  ###clear()
  #print(f"{logo}\n")

def blackjack():
    #screen_wipe()
    print(f"\n Blackjack time baby\n")
    start = input("Would you like a hand? y/n \n")
    #screen_wipe()
    if start == "y":

      hands = {
         "computer": [],
          "player": [],
          "score_player": [],
          "score_computer": [],
      }

      def deal():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

      global computer
      computer = hands["computer"]
      computer += [deal(), deal()]
      global score_computer
      score_computer = hands["score_computer"]
      score_computer = sum(computer)
      global player
      player = hands["player"]
      player += [deal(), deal()]
      global score_player
      score_player = hands["score_player"]
      score_player = sum(player)
      if score_player == 21:
          print ("Blackjack!")
        
      def update():
        hands["score_computer"] = sum(computer)
        hands["score_player"] = sum(player)
        global score_computer
        score_computer = hands["score_computer"]
        global score_player
        score_player = hands["score_player"]


      print(f'The dealer has a {computer[0]}\n')
      print(f"Your hand is {player[0]} and {player[1]} -> {score_player}\n\n ")

      def checker():
        update()
        for _ in range(len(player)):
          if score_player > 21 and 11 in player:
            player[(player.index[11])] = 1
            update()
        if score_player == score_computer:
            print(f"It's a draw!\n\n Your hand was {player} -> {score_player}\n\n The computer hand was {computer} -> {score_computer}\n\n")
            return False
        elif score_computer < score_player < 22:
            print(f"You win!\n\n Your hand was {player} -> {score_player}\n\n The computer hand was {computer} -> {score_computer}\n\n")
            return False
        elif score_computer > 21 >= score_player:
            print(f"You win!\n\n Your hand was {player} -> {score_player}\n\n The computer hand was {computer} -> {score_computer}\n\n")
            return False
        else:
            print(f"Dealer wins!\n\n\ Your hand was {player} -> {score_player}\n\n The computer hand was{computer} -> {score_computer}\n\n")
            return False

      def dealer_bust():
        update()
        while score_computer != 21 and score_computer < 17:
            computer.append(deal())
            update()
            if score_computer == 21:
              break
            elif score_computer > 21:
              if 11 in computer:
                computer[(computer.index(11))] = 1
                update()
                pass
              else:
                break
            else:
                continue
      def hit_stay():
          update()
          hitting = True
          while hitting:
              hitter = input("Would you like to hit or stay? hit/stay \n")
              #screen_wipe()
              if hitter == "hit":
                  player.append(deal())
                  update()
                  if score_player > 21:
                    if score_player > 21 and 11 in player:
                        for _ in range(len(player)):
                            if score_player > 21 and 11 in player:
                                player[(player.index(11))] = 1
                                update()
                        print(f"Your have {player} -> {score_player}")     
                        pass    
                    else:
                            print("You have busted!\n")
                            print(f"The dealer had {computer} -> {score_computer}\n")
                            print(f"You had {player} -> {score_player}")
                            hitting = False
                  elif score_player == 21 and score_computer != 21:
                      print("Blackjack!!!")
                      print(f"The dealer had {computer} -> {score_computer}\n")
                      print(f"You had {player} -> {score_player}")
                      hitting = False
                  else:
                    print(f"You have {player} -> {score_player}")
                    pass
              else:
                  hitting = checker()
      dealer_bust()
      hit_stay()
    else:
      print("Hmmm ok?\n\n")
      pass

if input("Would you like to play Blackjack? y/n \n") == "y":
    ##clear()
    go = True
    while go:
        blackjack()
        if input("Would you like to play again? y/n \n") == "y":
            #screen_wipe()
            continue
        else:
            go = False