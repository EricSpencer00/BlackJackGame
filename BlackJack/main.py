import random

print("Welcome to the Command Line Blackjack!")

# Default value
money = 5000
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def pick_random_card():
    return random.choice(ranks)

def calculate_hand_value(cards):
    value = 0
    num_aces = 0
    for card in cards:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            num_aces += 1
        else:
            value += int(card)

    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

def play_round(money):
    bet = int(input("How much do you want to bet? "))
    print(" * * * * ")
    if bet > money:
        print("You don't have enough money!")
        return money

    user_cards = [pick_random_card(), pick_random_card()]
    dealer_cards = [pick_random_card(), pick_random_card()]

    print("The Dealer has dealt you a " + user_cards[0] + 
          " and a " + user_cards[1] + 
          " and the Dealer is showing a " + dealer_cards[1])

    user_blackjack: bool = False
    while True:
        hand_value = calculate_hand_value(user_cards)
        print("Your hand:", " ".join(user_cards) + ", Your hand value:", hand_value)
        if hand_value == 21:
            winning = 1.5 * bet
            money += winning
            print("Blackjack! You win $" + str(winning))
            user_blackjack = True
            break
        elif hand_value > 21:
            print("Bust! Loser")
            money -= bet
            break

        action = input("Do you want to hit or stand? (h/s) ")
        if action.lower() == "h":
            user_cards.append(pick_random_card())
            print("You drew:", user_cards[-1])
            print(" * * * * ")
        elif action.lower() == "s":
            print("Standing...")
            print(" * * * * ")
            break

        print("Dealer was showing a " + dealer_cards[0] + " and has revealed a " + dealer_cards[1] + "...")
        print("Dealer's hand value: " + str(calculate_hand_value(dealer_cards)))
        print(" * * * * ")
    
    if (hand_value <= 21 and not user_blackjack):
        while calculate_hand_value(dealer_cards) < 17:
            new_card = pick_random_card()
            dealer_cards.append(new_card)
            print("Dealer drew:", new_card)

        dealer_hand_value = calculate_hand_value(dealer_cards)
        print("Dealer's hand value:", dealer_hand_value)

        if dealer_hand_value > 21:
            print("Dealer busts! You win!")
            money += 2 * bet
        elif dealer_hand_value > hand_value:
            print("Dealer wins!")
            money -= bet
        elif dealer_hand_value < hand_value:
            print("You win!")
            money += 2 * bet
        else:
            print("It's a push!")

    return money

while money > 0:
    print("You have $" + str(money) + " to play.")
    money = play_round(money)
    if money <= 0:
        print("You are out of money!")
        break

    print("You have $" + str(money))
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
