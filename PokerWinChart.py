"""suit_remover takes in a list of cards the argument.
The function will go through a list of cards and remove the suit from each card.
This can be used if you don't care about the suit of a card and need to have the cards turned into numbers.
I have no function to undo this like I do with hand_to_num and num_to_hand"""


def suit_remover(x):
    count = 0
    while count != len(x):
        for y in x:
            if y[-1] == '♥':
                x[count] = x[count].replace('♥', '')
                count += 1
            elif y[-1] == '♠':
                x[count] = x[count].replace('♠', '')
                count += 1
            elif y[-1] == '♦':
                a = x[count]
                x[count] = x[count].replace('♦', '')
                count += 1
            elif y[-1] == '♣':
                a = x[count]
                x[count] = x[count].replace('♣', '')
                count += 1
            else:
                count += 1
        return x


"""hand_to_num takes in a list of cards as the argument. 
The function will go through your list of cards and assign values like, A = 14, K = 13, Q = 12, and J = 11
This is the opposite effect of the num_to hand function."""


def hand_to_num(x):
    count = 0
    while count != len(x):
        for y in x:
            if y[0][0] == 'A':
                x[count] = x[count].replace('A', '14')
                count += 1
            elif y[0][0] == 'K':
                x[count] = x[count].replace('K', '13')
                count += 1
            elif y[0][0] == 'Q':
                x[count] = x[count].replace('Q', '12')
                count += 1
            elif y[0][0] == 'J':
                x[count] = x[count].replace('J', '11')
                count += 1
            else:
                count += 1
        return x


"""num_to_hand takes in a list of cards (numbers that are strings) as the argument. 
The function will go through your list of str(nums) and assign values like, 14 = A, 13 = K, 12 = Q, and 11 = J
This is the opposite effect of the hand_to_num function"""


def num_to_hand(x):
    count = 0
    while count != len(x):
        for y in x:
            if y[0:2] == '14' or x == '14':
                x[count] = x[count].replace('14', 'A')
                count += 1
            elif y[0:2] == '13' or x == '13':
                x[count] = x[count].replace('13', 'K')
                count += 1
            elif y[0:2] == '12' or x == '12':
                x[count] = x[count].replace('12', 'Q')
                count += 1
            elif y[0:2] == '11' or x == '11':
                x[count] = x[count].replace('11', 'J')
                count += 1
            else:
                count += 1
        return x


"""Finding High Card"""

"""find_high_card takes exactly two arguments, a player hand (a list of 2 cards) and the board (a list of up to 5 cards) 
The Board is a list of the flop cards, the turn card, and the river card. 
Although you don't need all three (the flop, turn and river). 
You could just have the flop cards (the first three to flop on the board)"""


def find_high_card(player_hand, the_board):
    player_hand = hand_to_num(player_hand)
    the_board = hand_to_num(the_board)
    number_list = []
    number_list_str = []
    for x in player_hand:
        the_board.append(x)
        suit_remover(the_board)
    for x in the_board:
        number_list.append(int(x))
    number_list = sorted(number_list)
    for x in number_list:
        number_list_str.append(str(x))
    number_list_str = num_to_hand(number_list_str)
    return f"{number_list_str[-1]} is High Card"


player_cards = ['J♦', '6♣']
card_list = ['8♥', '8♣', '6♠', 'Q♥', '9♥']
print(find_high_card(player_cards, card_list))


"""Finding a Pair"""

"""find_pair takes exactly two arguments, a players hand (a list of 2 cards) and the board (a list of up to 5 cards).
It will go through all the cards and return the top card you paired with."""


def find_pair(player_hand, the_board):
    player_hand = suit_remover(player_hand)
    the_board = suit_remover(the_board)
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    pair_list = []
    for x in player_hand:
        the_board.append(x)
    for x in cards:
        if the_board.count(x) == 2:
            pair_list.append(x)
    if len(pair_list) > 0:
        return f"You paired {pair_list[0]}s"
    else:
        return "You didn't pair anything!"


player_cards = ['J♦', '6♣']
card_list = ['8♥', '8♣', '6♠', 'Q♥', '9♥']
print(find_pair(player_cards, card_list))


"""Finding Two Pair"""


def find_two_pair(player_hand, the_board):
    player_hand = suit_remover(player_hand)
    the_board = suit_remover(the_board)
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    pair_list = []
    for x in player_hand:
        the_board.append(x)
    for x in cards:
        if the_board.count(x) == 2:
            pair_list.append(x)
    if len(pair_list) == 2:
        return f"You got two pair: {pair_list[0]}s, and {pair_list[1]}s"
    else:
        return "You didn't get two pair anything!"


player_cards = ['J♦', '6♣']
card_list = ['8♥', '8♣', '6♠', 'Q♥', '9♥']
print(find_two_pair(player_cards, card_list))


"""Finding Trips (Three of a kind)"""


def find_three_of_a_kind(player_hand, the_board):
    player_hand = suit_remover(player_hand)
    the_board = suit_remover(the_board)
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    pair_list = []
    for x in player_hand:
        the_board.append(x)
    for x in cards:
        if the_board.count(x) == 3:
            pair_list.append(x)
    if len(pair_list) == 1:
        return f"You got three of a kind with {pair_list[0]}s"
    else:
        return "You didn't get three of a kind!"


player_cards = ['2♥', '8♦']
card_list = ['8♥', '3♠', '9♦', '7♥', '4♠']
print(find_three_of_a_kind(player_cards, card_list))