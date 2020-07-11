word = input()
croatia_alphabets = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')

for alphabet in croatia_alphabets:
    word = word.replace(alphabet, "0")

print(len(word))
