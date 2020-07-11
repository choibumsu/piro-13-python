def checkGroup(word):
    alphabets = set()

    for letter in word:
        if letter in alphabets and last_alphabet is not letter:
            return False
        else:
            alphabets.add(letter)

        last_alphabet = letter

    return True


num = int(input())
result = 0
for _ in range(num):
    if checkGroup(input()):
        result += 1

print(result)
