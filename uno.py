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