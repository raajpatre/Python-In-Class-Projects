import random

target = list("python")

current = list("aaaaaa")

alphabet = "abcdefghijklmnopqrstuvwxyz"

attempts = 0


def get_random_char():

    return random.choice(alphabet)
i=0
while("".join(current)!="".join(target)):
    while(i<len(target) and current[i]!=target[i]):
        attempts=0
        for ch in alphabet:
            if ch==target[i]:
                current[i]=ch
                i+=1
                break
            else:
                attempts+=1
        print("".join(current)," attempts: ",attempts)

        
# Student Challenge:

# Write a loop that continues until 'current' equals 'target'.

# Inside, loop through each index (0 to 5).

# If current[i] is NOT the target letter, replace it with a new random char.

# If it IS the target letter, do nothing (keep it locked).