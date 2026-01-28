import random
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        # print(roll,"roll was 100, you lose. What are the odds?! Play again!")
        return False
    elif roll <= 50:
        # print(roll, "roll was 1-50, you lose. Play again!")
        return False
    elif 100 > roll > 50:
        # print(roll, "roll was 51-99, you win!")
        return True

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    current_wager = 1
    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)
        current_wager += 1

    # if value < 0:
    #     value = "broke"
    # print("Funds:", value)
    plt.plot(wX, vY)

n = 0
while n < 100:
    simple_bettor(10000, 100, 100)
    n += 1

plt.ylabel("Account Value")
plt.xlabel("Wager Count")
plt.show()







