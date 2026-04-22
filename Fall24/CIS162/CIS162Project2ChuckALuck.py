'''
Carson Wertz
This program simulates the dice game Chuck a Luck
and allows the player to roll the dice and make bets.

I certify that this code is mine, and mine alone, in accordance
with GVSU academic honesty policy.

Completed 10/16/2024
'''
# Imports
import random


# Rolls 3 random integers between 1 and 6 (inclusive) to use as dice values.
def roll_dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    print(f"Dice: {d1}, {d2}, {d3}")
    return (d1, d2, d3)


# Checks if two dice match one value.
def has_pair(val1, val2, val3, num):
    if ((val1 == num) and (val2 == num)) or ((val2 == num) and (val3 == num)) or ((val1 == num) and (val3 == num)):
        return True
    else:
        return False


# Checks if all 3 dice are the same value.
def is_triplets(val1, val2, val3):
    if (val1 == val2) and (val1 == val3):
        return True
    else:
        return False


# Makes a large bet, where the player gets 2 credits if the sum of
# all 3 dice is greater than 10 and is not a triplet.
def bet_large(val1, val2, val3):
    credits = -1
    total = val1 + val2 + val3
    if (total > 10) and (is_triplets(val1, val2, val3) == False):
        credits += 2
    return credits


# Makes a small bet, where the player gets 2 credits if the sum of
# all 3 dice is less than 11.
def bet_small(val1, val2, val3):
    credits = -1
    total = val1 + val2 + val3
    if (total < 11) and (is_triplets(val1, val2, val3) == False):
        credits += 2
    return credits


# Makes a field bet, where the player gets 2 credits if the sum of
# all 3 dice is outside the range of 8-12 (less than 8, greater than
# 12).
def bet_field(val1, val2, val3):
    credits = -1
    total = val1 + val2 + val3
    if ((total < 8) or (total > 12)) and (is_triplets(val1, val2, val3) == False):
        credits += 2
    return credits


# Makes a number bet, where the player can get 11, 3, or 2 credits depending
# on if 3, 2, or 1 dice values matches the number the player bets on.
def bet_number(val1, val2, val3, num):
    credits = -1
    if (is_triplets(val1, val2, val3) == True) and (val1 == num):
        credits += 11
    elif (has_pair(val1, val2, val3, num) == True) and ((val1 == num) or (val2 == num)):
        credits += 3
    elif (val1 == num) or (val2 == num) or (val3 == num):
        credits += 2
    return credits


# Prompts the player to make a bet. Includes error checking to remove
# any characters that are not valid in play_one_round.
def place_bets():
    bets = input("Place bets: ")
    bets_valid = ''
    for char in bets:
        if char in ["l", "s", "f"] or (char.isdigit() and 1 <= int(char) <= 6) or char == "q":
            bets_valid += char
    bets = bets_valid
    return bets


# Puts together the dice roll and bet functions to simulate one
# Chuck a Luck round.
def play_one_round(bets, credits):
    val1, val2, val3 = roll_dice()
    for bet in bets:
        if bet == "1":
            credits += bet_large(val1, val2, val3)
        elif bet == "s":
            credits += bet_small(val1, val2, val3)
        elif bet == "f":
            credits += bet_field(val1, val2, val3)
        elif bet.isdigit():
            credits += bet_number(val1, val2, val3, int(bet))
    print(f"Credits: {credits}")
    return credits


# Plays the game normally, prompting a user for a new bet every turn
# unless they quit or don't have enough credits to make their bet.
def play(credits):
    while credits > 0:
        bets = place_bets()
        if bets == "q":
            break
        elif credits <= 0:
            print("You do not have enough credits for these bets.")
            exit()
        play_one_round(bets, credits)
    print("Thanks for playing!")


# Plays the game until the player is out of credits, only
# taking in one bet at the start and using it for every round.
# Increments the amount of rounds played every turn.
def play_until_broke(bets, credits):
    rounds = 1
    while credits > 0:
        credits = play_one_round(bets, credits)
        rounds += 1
    print(f"Rounds: {rounds}")
    return rounds


# Instructor test code.
if __name__ == "__main__":
    print(place_bets())
    # play(5)