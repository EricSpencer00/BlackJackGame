import random

print("Welcome to the text-based BlackJack game!")

money: int = 5000
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def pick_random_card():
    return random.choice(ranks)

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
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


while money > 0:
    print("You have $" + str(money) + " to play.")
    user_input = int(input("How much do you want to bet?"))
    if money >= user_input:
        bet = user_input
        money -= bet
    else:
        bet = money
        money = 0

    user_cards = [pick_random_card(), pick_random_card()]
    dealer_cards = [pick_random_card(), pick_random_card()]

    print("The Dealer has dealt you a " + user_cards[0] + 
          " and a " + user_cards[1] + 
          " and the Dealer is showing a " + dealer_cards[1])
    
    if user_cards[0] == user_cards[1]:
        split_option = input("You have two of the same card, want to split? (y/n)")
        if split_option.lower() == "y":
            split_hand = [user_cards[0], pick_random_card()]
            user_cards = [split_hand, [user_cards[1], pick_random_card()]]
            print("You have split")
        else:
            print("You have not split")
    
    for hand in user_cards:
        while True:
            print("Your hand:", hand)
            hand_value = calculate_hand_value(hand)
            print("Your hand value:", hand_value)
            if hand_value == 21:
                winning: int = 1.5 * bet
                money += winning
                print("Blackjack! you win $" + str(winning))
                break
            elif hand_value > 21:
                print("Bust! Loser")
                break

            action = input("Do you want to hit or stand?")
            if action.lower() == "h":
                hand.append(pick_random_card())
                print("You drew:", hand[-1])
            elif action.lower() == "s":
                break
    
    if hand_value <= 21:
        while calculate_hand_value(dealer_cards) < 17:
            dealer_cards.append(pick_random_card())
            print("Dealer drew:", dealer_cards[-1])

        dealer_hand_value = calculate_hand_value(dealer_cards)
        print("Dealer's hand value:", dealer_hand_value)

        if dealer_hand_value > 21:
            print("Dealer busts! You win!")
            money += 2 * bet
        elif dealer_hand_value > hand_value:
            print("Dealer wins!")
        elif dealer_hand_value < hand_value:
            print("You win!")
            money += 2 * bet
        else:
            print("It's a push!")
            money = bet

        if money <= 0:
            print("You spent all your money!")
            break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break