"""import random

coin = random.choice(["heads","tails"])
print(coin)"""

"""from random import choice

print(choice(["heads","tails"]))"""

import random 

"""print(random.randint(1,10))"""

cards = ["Jack","King","Queen"]
random.shuffle(cards)
for card in cards:
    print(card)
