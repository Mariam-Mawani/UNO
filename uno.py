import random

print("----------------------------------------------------------------------------------------------------------------------------")
print("")
print("Welcome to: ")


print(r"""                               .-') _                                 ('-.     _  .-')  _ .-') _        
                             ( OO ) )                               ( OO ).-.( \( -O )( (  OO) )       
             ,--. ,--.   ,--./ ,--,'  .-'),-----.          .-----.  / . --. / ,------. \     .'_       
             |  | |  |   |   \ |  |\ ( OO'  .-.  '        '  .--./  | \-.  \  |   /`. ',`'--..._)      
             |  | | .-') |    \|  | )/   |  | |  |        |  |('-..-'-'  |  | |  /  | ||  |  \  '      
             |  |_|( OO )|  .     |/ \_) |  |\|  |       /_) |OO  )\| |_.'  | |  |_.' ||  |   ' |      
             |  | | `-' /|  |\    |    \ |  | |  |       ||  |`-'|  |  .-.  | |  .  '.'|  |   / :      
            ('  '-'(_.-' |  | \   |     `'  '-'  '      (_'  '--'\  |  | |  | |  |\  \ |  '--'  /      
              `-----'    `--'  `--'       `-----'          `-----'  `--' `--' `--' '--'`-------'       
                                             ('-.     _   .-')       ('-.                              
                                            ( OO ).-.( '.( OO )_   _(  OO)                             
                                ,----.      / . --. / ,--.   ,--.)(,------.                            
                               '  .-./-')   | \-.  \  |   `.'   |  |  .---'                            
                               |  |_( O- ).-'-'  |  | |         |  |  |                                
                               |  | .--, \ \| |_.'  | |  |'.'|  | (|  '--.                             
                              (|  | '. (_/  |  .-.  | |  |   |  |  |  .--'                             
                               |  '--'  |   |  | |  | |  |   |  |  |  `---.                            
                                `------'    `--' `--' `--'   `--'  `------'                            
 """)



# Create the unodeck
def deck_of_cards():
    deck = []
    colours = ["blue", "red", "yellow", "green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "skip", "reverse", "draw 2"]
    wild_cards = ["wild draw 4", "wild card"]

    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            # Two of each card, excluding 0
            if value != 0: 
                cardVal = "{} {}".format(colour, value)
                deck.append(cardVal)

    # Add wild cards
    for i in range(4):
        deck += wild_cards
    return deck


# Draw cards from deck
def draw_cards(cardnumber):
    cardsdrawn = []
    for x in range(cardnumber):
        cardsdrawn.append(unodeck.pop(0))
    return cardsdrawn


# Display player hands
def hand(player, playerhand):
    print("----------------------------------------")
    print("Player {}".format(player + 1))
    print("Your hand is: ")
    print("----------------------------------------")

    i = 1
    for card in playerhand:
        print("{}) {}".format(i, card))
        i += 1
    print("")


# check choice of cards to play
def play_choice(colour, value, hand):
    for card in hand:
        if "wild" in card:  # Wild cards can always be played
            return True
        elif colour in card or value in card:
            return True
    return False


# setup game & shuffle the decck
unodeck = deck_of_cards()
random.shuffle(unodeck)
discard = []
print(unodeck)


# play turns and starting cards.
players = [draw_cards(7), draw_cards(7)]
playturn = 0    # player 1 starts
playdirection = 1
playing = True


# account for top card, on the discard pile
discard.append(unodeck.pop(0))
splitcard = discard[0].split(" ", 1)
playcolour = splitcard[1]

if playcolour != "wild":
    cardVal = splitcard[1]
else:
    cardVal = "Any"
print(f"\nStarting card: {discard[-1]}")    # show card(discard)


# main game loop
while playing:
    current_player = playturn
    current_hand = players[current_player]

    if current_player == 0:
        hand(current_player, current_hand)  # player 1 turn
        print("The top card, on the discard pile is: {}".format(discard[-1]))

        # check existing playable cards
        if play_choice(playcolour, cardVal, current_hand):
            cardchosen = int(input("Which card do you choose to play? ")) - 1
            chosen_card = current_hand[chosen_card]

            # validate card
            while not play_choice(playcolour, cardVal, [chosen_card]):   # check how many cards they have after each play
                cardchosen = int(input("Invalis card, please choose again. ")) - 1
                chosen_card = current_hand[cardchosen]
            print("You played: {}".format(chosen_card))
            discard.append(current_hand.pop(cardchosen))    # remove card from player hand

        else:
             print("No playable cards. Drawing one...")     # automatically draws one card
             current_hand.extend(draw_cards(1))
             pass

    else:
        # account for computer
        print("Computer's turn...")
        playable = [c for c in current_hand if play_choice(playcolour, cardVal, [c])]

        if playable:
            chosen_card = random.choice(playable)
            print("Computer played: {}".format(chosen_card))
            discard.append(chosen_card)
            current_hand.remove(chosen_card)
        else:
            print("Computer draws a card.")
            current_hand.extend(draw_cards(1))
            pass


    # how wild cards affect the game
    splitcard = discard[-1].split(" ", 1)   # last card to be discarded
    playcolour = splitcard[0]
    if len(splitcard) == 1:     # only a wild and nothing after it.
        cardVal = "Any"
    else:
        cardVal = splitcard[1]

    # handling wild cards
    if playcolour == "wild":
        if current_player == 0:
            print("choose a new colour: ")
            i = 1
            for card in ["blue", "red", "yellow", "green"]:
                print("{} {}".format(i, card))
                i += 1
            newcolour = int(input("Colour chosen is: "))
            playcolour = ["red", "yellow", "green", "blue"][newcolour]
        else:
            playcolour = random.choice(["red", "yellow", "green", "blue"])
            print("Computer changed the colour to: {}".format(playcolour))