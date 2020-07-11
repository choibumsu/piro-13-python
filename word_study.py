word = input().upper()
alphabets = {}

for letter in word:
    alphabets[letter] = alphabets[letter] + 1 if letter in alphabets else 1

alphabets = sorted(alphabets.items(), key=(lambda x: x[1]), reverse=True)

if len(alphabets) > 1 and alphabets[0][1] == alphabets[1][1]:
    print("?")
else:
    print(alphabets[0][0])
