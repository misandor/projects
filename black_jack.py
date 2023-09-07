import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
          'Ace': 11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except ValueError:
            print("Sorry, but need to be an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry your bet can't exceed ", chips.total)
            else:
                break


# function for take a new card
def take_hit(deck, hand):
    single_card = deck.deal_card()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# function for continue taking card or stand
def hit_or_stand(deck, hand, playing=True):
    while True:
        x = input("Hit or Stand? Enter y or n: ")
        if x == 'y':
            take_hit(deck, hand)
        elif x == 'n':
            print("Player stands.")
            break
        else:
            print("Please insert y or n")
            continue
    return playing


# display cards
def show_cards(player, dealer):
    # show only one of the dealer cards
    print("\n Dealer Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # show all player cards
    print("\n Player Hand: ")
    for card in player.cards:
        print(card)


def show_all_cards(player, dealer):
    # show all dealer cards + calculate
    print("\n Dealer Hand: ")
    for card in player.cards:
        print(card)
    print(f'Value of Dealer hand is {dealer.value}')

    # show all players cards
    print("\n Player Hand: ")
    for card in player.cards:
        print(card)
    print(f'Value of player hand is {player.value}')

# function to handle end of the game
def player_lose(player, dealer, chips):
    print("Bust Player")
    chips.lose_bet()


def player_win(player, dealer, chips):
    print("Player Win")
    chips.win_bet()


def dealer_lose(player, dealer, chips):
    print("Bust Dealer")
    chips.lose_bet()


def dealer_win(player, dealer, chips):
    print("Dealer win")
    chips.win_bet()


def push(player, dealer):
    print("Dealer and Player tie")


# game play

while True:
    # Print an opening statement
    print("Welcome to BlackJack. The first who achieved 21 or go as close as possible WON!")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    # Set up the Player's chips
    player_chips = Chips()
    # Prompt the Player for their bet
    take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    show_cards(player_hand, dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_cards(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_lose(player_hand, dealer_hand, player_chips)
        break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value < 21:
        while dealer_hand.value < player_hand.value:
            take_hit(deck, dealer_hand)
        # Show all cards
        show_all_cards(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_lose(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
        # Inform Player of their chips total
    print(f"\n Player total chips are {player_chips.total}")
    # Ask to play again
    new_game = input("Would you like to play again? y or n: ")
    if new_game == 'y':
        playing = True
    elif new_game == 'n':
        break
    else:
        print("Thank's for playing!!!! Good bye")
        break
