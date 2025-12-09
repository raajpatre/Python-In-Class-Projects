text = input("Enter text: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

counts = [0] * 26  # Creates a list of 26 zeros


# Step 1: Count frequencies

for i in range(len(text)):
    if text[i] in alphabet:
        counts[alphabet.index(text[i])]+=1
        
# Step 2: Draw the chart
print("Frequency Graph:")

for i in range(26):
    if counts[i] > 0:
        print(alphabet[i]," ",end="")
        for j in range(counts[i]):
            print("#",end="")
        print()
