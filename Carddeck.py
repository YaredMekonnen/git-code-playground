import random
# BIG CODE COMMENT
''' 
OPTION 1

The change that I added is that when the PlayingCard is initialized it will have a color attribute too
and I also added a method to get the color of the Playing card since that it is not initialized from a passed argument, instead
if the suite is heart or diamond it will be red. So that's why I used the getcolor method. I called the method to get print with the card.
################
Here's the pre-shuffled deck: [2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♠, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♣, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♡, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, A♢]
Here's the deck after the shuffle: [J♡, 4♠, 7♡, 9♢, 6♢, 4♣, 8♡, 10♢, 9♠, A♠, Q♣, 5♣, 2♠, 8♠, 3♡, A♣, J♠, K♡, 6♡, 5♠, 3♣, 9♣, 7♠, J♢, 8♢, 5♢, 4♢, A♢, 6♣, 2♣, 10♠, 10♣, 9♡, 3♢, 8♣, K♠, 7♢, 6♠, 7♣, 5♡, Q♢, Q♡, K♣, Q♠, K♢, A♡, J♣, 3♠, 2♢, 10♡, 4♡, 2♡]
Player 1: 2♡ red , Player 2: 4♡ red
Player 2 wins this hand.
Player 1: 10♡ red , Player 2: 2♢ red
Player 1 wins this hand.
Player 1: 3♠ black , Player 2: J♣ black
Player 2 wins this hand.
Player 1: A♡ red , Player 2: K♢ red
Player 1 wins this hand.
Player 1: Q♠ black , Player 2: K♣ black
Player 2 wins this hand.
Player 1: Q♡ red , Player 2: Q♢ red
This hand is a draw.
Player 1: 5♡ red , Player 2: 7♣ black
Player 2 wins this hand.
Player 1: 6♠ black , Player 2: 7♢ red
Player 2 wins this hand.
Player 1: K♠ black , Player 2: 8♣ black
Player 1 wins this hand.
Player 1: 3♢ red , Player 2: 9♡ red
Player 2 wins this hand.
Player 1: 10♣ black , Player 2: 10♠ black
This hand is a draw.
Player 1: 2♣ black , Player 2: 6♣ black
Player 2 wins this hand.
Player 1: A♢ red , Player 2: 4♢ red
Player 1 wins this hand.
Player 1: 5♢ red , Player 2: 8♢ red
Player 2 wins this hand.
Player 1: J♢ red , Player 2: 7♠ black
Player 1 wins this hand.
Player 1: 9♣ black , Player 2: 3♣ black
Player 1 wins this hand.
Player 1: 5♠ black , Player 2: 6♡ red
Player 2 wins this hand.
Player 1: K♡ red , Player 2: J♠ black
Player 1 wins this hand.
Player 1: A♣ black , Player 2: 3♡ red
Player 1 wins this hand.
Player 1: 8♠ black , Player 2: 2♠ black
Player 1 wins this hand.
Player 1: 5♣ black , Player 2: Q♣ black
Player 2 wins this hand.
Player 1: A♠ black , Player 2: 9♠ black
Player 1 wins this hand.
Player 1: 10♢ red , Player 2: 8♡ red
Player 1 wins this hand.
Player 1: 4♣ black , Player 2: 6♢ red
Player 2 wins this hand.
Player 1: 9♢ red , Player 2: 7♡ red
Player 1 wins this hand.
Player 1: 4♠ black , Player 2: J♡ red
Player 2 wins this hand.
Player 1 score: 12 , Player 2 score: 12
The game is a tie :(

    
    
    
    
    
    
    
    
    
    
    
'''



class PlayingCard:
    
    def __init__(self,v,s):
        
        if type(v) != type(1) or v > 14 or v < 2:
            raise Exception("A PlayingCard's value must be an integer in the range 2-14.")
        self.__value = v
        self.__suit = s
        if s in ["♠", "♣"]:
            self.__color = "black"
        elif s in ["♡", "♢"]:
            self.__color = "red"
        else:
            raise Exception("Invalid suit: " + s)
        
    def __repr__(self):
        printval = self.__value
        if self.__value == 11:
            printval = "J"
        elif self.__value == 12:
            printval = "Q"
        elif self.__value == 13:
            printval = "K"
        elif self.__value == 14:
            printval = "A"
        return str(printval)+str(self.__suit)
    
    def __lt__(self,other):
        if self.__value < other.__value:
            return True
        else:
            return False
    def get_color(self):
        return self.__color



class Deck:
    
    def __init__(self):
        self.__card_list = []  #the deck will be initially empty
        
    def put_on_top(self,card):
        self.__card_list.append(card)
        
    def remove_from_top(self):
        if len(self.__card_list) == 0:
            raise Exception("This deck has no cards left.")
        else:
            return self.__card_list.pop()
        
    def shuffle(self):
        random.shuffle(self.__card_list)
        
    def __repr__(self):
        return str(self.__card_list)
    
    def is_empty(self):
        return (self.__card_list == [])
    






high_card_deck = Deck()

#create each of the 52 playing cards and put them in the deck
suits = ["♠","♣","♡","♢"]
for s in suits:
    for v in range(2,15):
        curr_card = PlayingCard(v,s)
        high_card_deck.put_on_top(curr_card)
        
#look at the deck both before and after shuffling        
print("Here's the pre-shuffled deck:",high_card_deck)
high_card_deck.shuffle()
print("Here's the deck after the shuffle:",high_card_deck)

#initialize both player's scores to 0
p1score = 0
p2score = 0

#keep going until all cards are dealt out
while not high_card_deck.is_empty():
    
    #draw a card for each player
    p1card = high_card_deck.remove_from_top()
    p2card = high_card_deck.remove_from_top()
    
    print("Player 1:",p1card,p1card.get_color(),", Player 2:",p2card,p2card.get_color())
    
    #check which player wins this hand
    if p1card > p2card:
        p1score += 1
        print("Player 1 wins this hand.")
    elif p1card < p2card:
        p2score += 1
        print("Player 2 wins this hand.")
    else:
        print("This hand is a draw.")
        

#Figure out who wins and display the game-end message
print("Player 1 score:",p1score,", Player 2 score:",p2score) 
if p1score > p2score:
    print("Player 1 wins the game!!!")
elif p2score > p1score:
    print("Player 2 wins the game!!!")
else:
    print("The game is a tie :(")
