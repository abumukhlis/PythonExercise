# Display 10 random numbers from interval [3, 7)
import random
for i in range(10):
    print(random.randrange(1, 7))

# Display 20 random outcomes
outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))
