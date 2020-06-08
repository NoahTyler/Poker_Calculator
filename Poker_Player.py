from random import choice


class Poker:
    cards = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥', 'A♠', 'K♠', 'Q♠', 'J♠',
             '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠', 'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦',
             '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣',
             '2♣']

    def __init__(self, player):
        self.player = player
        self.cards = Poker.cards
        self.cards_list = []
        self.chips = 100
        self.pot = 0
        self.hand = []

    def reset_deck(self):
        self.cards = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥', 'A♠', 'K♠', 'Q♠',
                      'J♠', '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠', 'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦',
                      '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣',
                      '5♣', '4♣', '3♣', '2♣']

    def deal_hand(self):
        single_card_1 = choice(self.cards)
        self.cards.remove(single_card_1)
        single_card_2 = choice(self.cards)
        self.cards.remove(single_card_2)
        self.hand.append(single_card_1)
        self.hand.append(single_card_2)
        return single_card_1, single_card_2

    def flop_cards(self):
        flop_card_1 = choice(self.cards)
        self.cards.remove(flop_card_1)
        flop_card_2 = choice(self.cards)
        self.cards.remove(flop_card_2)
        flop_card_3 = choice(self.cards)
        self.cards.remove(flop_card_3)
        self.cards_list.extend([flop_card_1, flop_card_2, flop_card_3])
        return flop_card_1, flop_card_2, flop_card_3

    def turn_card(self):
        turn_card = choice(self.cards)
        self.cards.remove(turn_card)
        self.cards_list.append(turn_card)
        return turn_card

    def river_card(self):
        river_card = choice(self.cards)
        self.cards.remove(river_card)
        self.cards_list.append(river_card)
        return river_card

    def show_hand(self):
        return f"{self.player} HAS {Poker.deal_hand(self)}"

    def place_bets(self):
        bet_size = input("How Much Do You Bet? ")
        self.chips -= int(bet_size)
        self.pot += int(bet_size) * 2

    def show_flop_turn_river(self):
        print(f"Your Cards: {self.hand}")
        input("Press Enter for Next")
        self.flop_cards()
        print(f"Your Cards: {self.hand}")
        print(f"THE CARDS: {self.cards_list}")
        input("Press Enter for Next")
        self.turn_card()
        print(f"Your Cards: {self.hand}")
        print(f"THE CARDS: {self.cards_list}")
        input("Press Enter for Next")
        self.river_card()
        print(f"Your Cards: {self.hand}")
        print(f"THE CARDS: {self.cards_list}")
        return 'fold'


def get_name():
    name = input("What is your name?\n")
    while len(name) == 0:
        print("Your name is not long enough!!")
        name = input("What is your name?\n")
    return name


def play_poker(name):
    player = Poker(name)
    player.reset_deck()
    print(player.show_hand())
    return player.show_flop_turn_river()


player_name = get_name()
play_poker(player_name)
yay_nay = 0
list_of_yes = ['y', 'yes', 'ya', 'yep', 'yeah', 'yup', 'you bet',
               "hell yeah", 'fuck yeah', "why wouldn't I", 'you know it']

