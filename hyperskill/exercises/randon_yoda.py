import random

sentence = input().split() # Converts the input sentence into a list of words
random.seed(43)

random.shuffle(sentence)
yoda = ' '.join(sentence)
print(yoda)

