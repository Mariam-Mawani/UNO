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
    def playchoice(colour, value, hand):
        for card in hand:
            if "wild" in card:  # Wild cards can always be played
                return True
            elif colour in card or value in card:
                return True
        return False