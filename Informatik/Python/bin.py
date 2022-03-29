print(bin(18))

def bin2(int):
    lst = []
    while int >= 1:
        lst.append(int % 2)
        int = int // 2 
        print(int)
    print(lst)
    
bin2(18)