
def split_it(strang):
    strang_one = ""
    strang_two = ""
    for i in range(len(strang)):
        if (strang[i] == ("_")) or (strang[i] == (".")) or (strang[i].islower() == True):
            strang_one = strang_one + strang[i]

        elif (strang[i] == ("|")) or strang[i] == (" ") or (strang[i].isupper() == True):
            strang_two = strang_two + strang[i]

    return strang_one, strang_two

def split_rec(strang):
    def split_rec_lista(strang_lista,strang_one,strang_two):
        if len(strang_lista) == 0:
            return strang_one, strang_two
        if (strang_lista[0] == ("_")) or (strang_lista[0] == (".")) or (strang_lista[0].islower() == True):
            strang_one = strang_one + strang_lista[0]
        elif (strang_lista[0] ==  ("|")) or (strang_lista[0] ==  (" ")) or (strang_lista[0].isupper() == True):
            strang_two = strang_two + strang_lista[0]
        return split_rec_lista(strang_lista[1:], strang_one, strang_two)

    strang_lista = list(strang)
    strang_one = ""
    strang_two = ""

    strang_one, strang_two = split_rec_lista(strang_lista, strang_one, strang_two)

    return strang_one, strang_two

