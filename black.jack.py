 #+++++++++++++++++++Black Jack Game++++++++++++++++++
import random
from tkinter.messagebox import YES 
def make_deck():
  """create a deck of cards"""
  faces = [2,3,4,5,6,7,8,9,10,'A', 'J','Q','K']
  suits = ['♥','♠','♣','♦']
  cards= {}
  for face in faces :
    for suit in suits:
      if face == "A":
        value = 'A'         
      elif type(face) == type(0):
        value = face
      else:
        value = 10
      suit ="{} {}".format(face,suit)
      cards[suit] = value
  #keep print or return outside of the loop so it does not update the total everytime
  return cards 

#+++++++++++++++++++draw_card+++++++++++++++++++++++++++++

def draw_card(hand,hide = False):
  """ drawing a card templete and using it for my deck"""
  i = 0
  for card in hand:
    face = card.split()[0]
    suit = card.split()[1]
    if hide == True and i == 0:
        suit = face = "#"
    i += 1 

    print( """
     ____________
    |  {}         |
    | {}          |
    |             yes|
    |          {} |
    |         {}  |
    |_____________|""".format(suit,face,suit,face))
    


#++++++++++++++pick the players hand+++++++++++++++++++++

def pick_hands_players(cards,player1_hand=[],player1_total=0, turns=2):
  """ choose a card for the player from a deck of card for two continus round"""
  #assigning variables 
  player1_total = player1_total
  player1_hand_temporary = []
  # making the keys a list to be able to use choice on it 
  keys = list(cards.keys())

   #pick 2 random cards 
  for turn in range(turns):
    player1_hand_temporary.append(random.choice(keys))

    # Removing the repeated keys
    keys.remove(player1_hand_temporary[turn])

    # condition for special suit
    if cards[player1_hand_temporary[turn]] == "A":
      print("Ace is been drawn for you")
      Ace_value = int(input("choose 1 or 11 as your ace value"))
      player1_total += Ace_value 
    else:
      player1_total += cards[player1_hand_temporary[turn]]
  player1_hand += player1_hand_temporary
  print("Your hand:") 
  draw_card(player1_hand)
  
  # Drawing the cards 
  print()
  print ("Your Total: \n {}".format(player1_total))
  return player1_hand, player1_total

#+++++++++++++++++dealer's hand++++++++++++++++++++

def pick_hands_dealer(cards,player2_hand=[], player2_total=0, turns=2):

  """this function pick the hand forthe dealer"""
  #assigning variables and making the keys a list to be able to use choice on it 
  keys = list(cards.keys())
  player2_total = player2_total
  player2_hand_temporary = []
  #choosing a random key from my dict  
  for turn in range(turns):
    player2_hand_temporary.append(random.choice(keys))
    keys.remove(player2_hand_temporary[turn])

    # Ace conditioning:
    if cards[player2_hand_temporary[turn]]== "A":
      if player2_total <= 10:
        Ace_value = 11 
      elif player2_total > 10:
        Ace_value = 1
      player2_total += Ace_value 
    else:
      player2_total += cards[player2_hand_temporary[turn]]
  player2_hand += player2_hand_temporary

  #Don't print total and cover the first card drawn 
  if turns == 2:
    print ("Dealer's hand:")
    draw_card(player2_hand,True)
    print ("""\nDealer's Total:
Not clear yet!""")
  # print the total for the turns where 2 cards were not drawn 
  if turns == 1:
    print ("Dealer's hand:")
    draw_card(player2_hand)
    print ("Dealer Total: \n {}".format(player2_total))
  return player2_hand, player2_total

#+++++++++++++++picking winner +++++++++++++++++++

def winner(name,player1_total, player2_total):
  """ choosing a winner"""

  #when a player is winner
  if player1_total > player2_total and player1_total < 21 :
    print("{} is the winner".format(name))
  elif player1_total > player2_total and player1_total == 21 :
    print("Nice!!! {} hit the black jack".format(name))
  elif player2_total > 21 and player1_total <21: 
    print("{} is the winner".format(name))

  # when the dealer is winner or game is a tie
  elif player2_total >player1_total and player2_total < 21:
    print("dealer is the winner")
  elif player1_total < player2_total and player2_total == 21 :
    print("Sorry {} lost!! dealer hit black jack!".format(name))
  elif player1_total > 21 and player2_total <21: 
    print("Dealer is the winner")

  #when nobody is winner 
  elif player1_total == player2_total == 21 :
    print("Game is a tie")
  elif player1_total > 21 and player2_total >21 :
    print("Nobody is winner")
  elif player1_total == player2_total:
    print("Game is a tie!")

#++++++++++++++++++playing the game +++++++++++++++++++++++++++
def play_black_jack():
  """This function is playing the main game"""
  #welcome and instruction
  print("   welcome to my BlackJack!!!\n")
  print(""" INSTRUCTIONS:The cards 2 through 10 are worth their face value. Kings, queens, and jacks are each worth 10, and aces may be used as either 1 or 11. The objective for the player is to draw cards totaling closer to 21, without going over, than the dealer's cards. You can draw as many as you want, but you will be the judge! The best total of all is a two-card 21, or a blackjack.\n""")

  #playing endless game with a condition to exit 
  while True:
    ready= (input("""
              Are you ready to play??
                Shuffeling...\n""")).lower()
    #condition to exit
    if ready != "yes":
      print("""
                See you next time!""")
      return
    #intracting with the player 
    player1_name = (input("""
              please enter player 1 name:\n""")).title()
    print("\n{} you are going to play against the dealer...\n".format(player1_name))
    print("Dealing Cards...\n")

    # calling my making a deck and hand functions and assiging a variables 
    deck_of_cards = make_deck()
    player1_hand,player1_total = pick_hands_players(deck_of_cards)
    print()
    player2_hand,player2_total =pick_hands_dealer(deck_of_cards)
    print()
  
    # giving the special condition of wether the player wants more    cards 
    hit_or_stand = "yes"
    while player1_total < 21 and hit_or_stand == "yes":
      hit_or_stand= input("Would you want another card?\n")
      if hit_or_stand =="yes":
        player1_hand,player1_total = pick_hands_players(deck_of_cards, 
        player1_hand = player1_hand,
        player1_total = player1_total,
        turns=1)
      else:
        break
    #dealer has to show their hand 
    print("Dealer hand was:")
    draw_card(player2_hand)
    print ("Dealer Total: \n {}".format(player2_total))

    # if dealer hand os less than 17, they can take more cards 
    #and runing the pick hand function 
    if player2_total < 17 :
      print("""\nDealer totsl is less than 17 so he/she has to draw more cards.\n 
       Drawing cards...""")
      player2_hand,player2_total = pick_hands_dealer(deck_of_cards, 
      player2_hand = player2_hand,
      player2_total = player2_total,
      turns=1)   
    # deciding the winner 
    print() 
    winner(player1_name,player1_total, player2_total)
  
play_black_jack()