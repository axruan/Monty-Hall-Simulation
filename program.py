# Alex Ruan
# I think you should switch.
#
# I won 350 without switching and 494 while switching

import random as r


def monty(switch):
  wins = 0

  for _ in range(1000):

    carDoor = r.randint(0, 2)
    chooseDoor = r.randint(0, 2)

    revealDoor = [0, 1, 2]

    for i in {carDoor, chooseDoor}:
      revealDoor.remove(i)

    revealDoor = r.choice(revealDoor)

    if switch:
      switchDoor = [0, 1, 2]
      switchDoor.remove(revealDoor)
      if chooseDoor == switchDoor[0]:
        chooseDoor = switchDoor[1]

      else:
        chooseDoor = switchDoor[1]

    if chooseDoor == carDoor:
      wins += 1

  print("Wins:", wins)


print("No switch:")
monty(False)
print("Switch:")
monty(True)

# Explanation: Imagine you have 10 doors, and you choose one - that first choice is random
# and you don't have any information on it. Then, eight doors are opened so that two doors remain, you can
# switch or not. You don't know anything about the one you chose, but you do know the other remaining door
# "beat" ther other 98 doors. Therefore, there is a higher probability that the prize is behind that door.
