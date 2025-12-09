import random
words = ["fresh", "prince", "of", "bel", "air", "fresh", "fruits", "are", "good"]
current_word = "fresh"
sentence = [current_word]

for _ in range(5):

    possible_next_words = []
    for i in range(len(words)-1):
        if words[i]==current_word:
            possible_next_words.append(words[i+1])

   

    # STUDENT TODO:

    # Iterate through the 'words' list (stop 1 before the end!).

    # If words[i] matches current_word, append words[i+1] to possible_next_words.

   

    if len(possible_next_words) > 0:

        next_word = random.choice(possible_next_words)

        sentence.append(next_word)

        current_word = next_word
    else:

        break

   

print("Generated:", " ".join(sentence))