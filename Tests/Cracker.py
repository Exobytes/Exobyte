import string
import random
import time

chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("Enter your target text: ")
attempt1 = ''.join(random.choice(chars) for i in range(len(target)))
attempt2 = ''

completed = False

generation = 0

while completed == False:
    print(attempt1)
    attempt2 = ''
    completed = True
    for i in range(len(target)):
        if attempt1[i] != target[i]:
            completed = False
            attempt2 += random.choice(chars)
        else:
            attempt2 += target[i]
    generation += 1
    attempt1 = attempt2
    time.sleep(0.2)

print("Target matched! That took " + str(generation) + " tries")