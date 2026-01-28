import random
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        # print(roll,"roll was 100, you lose. What are the odds?! Play again!")
        return False
    elif 1 < roll <= 50:
        # print(roll, "roll was 1-50, you lose. Play again!")
        return False
    elif 100 > roll > 50:
        # print(roll, "roll was 51-99, you win!")
        return True

def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    current_wager = 1
    previous_wager = "win"
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == "win":
            if rollDice():
                value += wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = "lose"
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value < 0:
                    break
            current_wager += 1
        elif previous_wager == "lose":
            if rollDice():
                value += previous_wager_amount*2
                previous_wager = "win"
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= previous_wager_amount*2
                previous_wager_amount = previous_wager_amount*2
                wX.append(current_wager)
                vY.append(value)
                if value < 0:
                    break
            current_wager += 1


    # print("Funds:", value)
    plt.plot(wX, vY)


doubler_bettor(10000, 100, 100)
plt.show()
