import random
words = ["hallo", "du", "sehr", "bin", "kreativ", "ich"]
sentence = []

for a in range (0, 5):
    for i in range (0, 5):
        sentence.append(words[random.randrange(0, len(words))])

    print(sentence)
    sentence.clear()

