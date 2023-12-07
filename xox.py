def input_valid(deger, tahta):
    if len(deger) != 2:
        print("Değer girerken satır - sütun olarak örneğin 1 - 2 ")
        return False
    try:
        if (1 <= int(deger[0]) <= 3) and (1 <= int(deger[1]) <= 3):
            
            if tahta[int(deger[0])-1][int(deger[1])-1] != '_':
                print("Bu kutucuk dolu")
                return False
            return True
        else:
            print("1 ile 3 arasında bir değer giriniz (1 ve 3 dahil)")
            return False
    except ValueError:
        print("1 ile 3 arasında bir değer giriniz (1 ve 3 dahil)")
        return False

def draw_board(deger, oyuncu, tahta):
    tahta[int(deger[0])-1][int(deger[1])-1] = oyuncu
    for linex in tahta:
        print(linex)

def gamefin(tahta):
    searcht = '_'

    for i in range(3):
        if len(set(tahta[i])) == 1:
            if tahta[i][1] == '_':
                continue
            elif tahta[i][1] == 'X':
                print("Oyun bitti! Kazanan 1. oyuncu")
            else:
                print("Oyun bitti! Kazanan 2. oyuncu")
            return True

    
    for i in range(3):
        if tahta[0][i] == tahta[1][i] == tahta[2][i]:
            if tahta[0][i] == '_':
                continue
            elif tahta[0][i] == 'X':
                print("Oyun bitti! Kazanan 1. oyuncu")
            else:
                print("Oyun bitti! Kazanan 2. oyuncu")
            return True

    
    if (tahta[0][0] == tahta[1][1] == tahta[2][2]) or (tahta[0][2] == tahta[1][1] == tahta[2][0]): 
        if tahta[1][1] == 'X':
            print("Oyun bitti! Kazanan 1. oyuncu")
        elif tahta[1][1] == 'O':
            print("Oyun bitti! Kazanan 2. oyuncu")
        else:
            return False
        return True

    
    for sublist in tahta:
        if searcht in sublist:
            return False

    print("Oyun bitti tahtada başka alan kalmadı")
    return True


def x_o():
    tahta = [['_']*3 for i in range(3)]
    turn = 1
    row_col = [0]

    while not gamefin(tahta):
        piece = '_'

        
        while not input_valid(row_col, tahta):
            oyuncu = turn % 2
            if oyuncu == 0:
                oyuncu = 2
                piece = 'O'
            else:
                piece = 'X'
            p1 = input('Oyuncu ' + str(oyuncu) + ' değerinizi giriniz: ')
            row_col = p1.split("-")

        draw_board(row_col, piece, tahta)

        row_col = [0]
        turn += 1


x_o()
