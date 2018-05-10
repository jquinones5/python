text = input("Enter a single line of text:\n")
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_num = {}
for letter in alphabet:
    alpha_num[letter] = 0
num_letters = 0
num_token = 0
for token in text:
    if not token.isspace():
        num_letters += 1
        alpha_num[token.upper()] += 1
    else:
        num_token += 1
print("The line contains {:d} letters.".format(num_letters))
print("The line contains {:d} string tokens.".format(num_token))
print("The frequency of each letter is")
for letter in alphabet:
    if alpha_num[letter] != 0:
        print("{} -- {:d}".format(letter,alpha_num[letter]))
