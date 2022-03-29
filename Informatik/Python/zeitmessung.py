import random
import time
def randArr():
    num = int(input('Enter the number of Samples you want to have? \n'))
    bereich = int(input('Enter the range of numbers (0-x)\n'))
    erg = []
    zeiten = []
    for i in range(0, num):
        start = time.time()
        erg.append(random.randrange(0, bereich))
        end = time.time()
        zeit = end - start
        zeiten.append(zeit)
    print("had {num} samples in range of 0-{bereich}\n min time: {min} sec \n max time: {max} sec\n total time: {total} secs".format(num=num, bereich = bereich, min = min(zeiten), max = max(zeiten), total = sum(zeiten)))

randArr()