import random


def ver():
    str = "hallo"
    lst = list(str)
    print(lst)
    print(str)
    shuffle = random.shuffle(lst)
    print(random.shuffle(lst))


ver()