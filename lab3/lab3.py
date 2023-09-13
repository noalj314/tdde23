
def new_board():
    return {}
board = new_board()

def place_piece(board, xplace, yplace, spelare):
    if is_free(board, xplace, yplace) == True:
        if spelare in board:
            koordinater = board.get(spelare)
            koordinater.append((xplace, yplace))
            board.update({spelare: koordinater})
            return True
        else:
            board.update({spelare: [(xplace, yplace)]})
            return True
    else:
        return False

def is_free(board, xfree, yfree):
    for i in board:
        if (xfree, yfree) in board[i]:
            return False
    else:
        return True

def get_piece(board, xpiece, ypiece):
    for spelare, koordinater in board.items():
        if (xpiece, ypiece) in koordinater:
            return spelare
    else:
        return False

def move_piece(board, xgammal, ygammal, xny, yny):
    for i in board:
        if (xgammal, ygammal) in board[i] and is_free(board, xny, yny) == True:
            index = board[i].index((xgammal, ygammal))
            board[i].pop(index)
            board[i].insert(index, (xny, yny))
            return True
    else:
        return False

def remove_piece(board, xbort, ybort):
    for i in board:
        if (xbort, ybort) in board[i]:
            index = board[i].index((xbort, ybort))
            board[i].pop(index)
            return True
    else:
        return False

def count(board, r_or_c, num, spelare):
    antal = 0
    if r_or_c == "column": # dvs x
        position = 0
    else:
        position = 1 # row dvs y
    if spelare in board:
        for i in board[spelare]:
            if i[position] == num:
                antal += 1
        return antal
    else:
        return False
def nearest_piece(board, xnarmsta, ynarmsta):
    narmast = None
    narmast_kord = False

    def jamfor(narmast, kandidat, narmast_kord):
        if narmast is None or narmast > kandidat:
            narmast = kandidat
            narmast_kord = (nuvarandex, nuvarandey)
        return narmast, narmast_kord

    for spelare, koordinater in board.items():
        for nuvarandex, nuvarandey in koordinater:
            kandidat = ((xnarmsta - nuvarandex) ** 2 + (ynarmsta - nuvarandey) ** 2) ** 0.5
            narmast, narmast_kord = jamfor(narmast, kandidat, narmast_kord)
    return narmast_kord

def fakultet(n,k):
    if k == 0 or k == n or n == 0:
        return 1
    if k >= (n-k):
        if n == (k+1):
            return n
        else:
            return n * fakultet(n - 1, k)
    if (n-k) >= k:
        if n == (n-k):
            return n
        else:
            return n * fakultet(n - 1, k)

def choose(n,k):
    if k > (n-k):
        return fakultet(n, k) // (fakultet((n-k), 1))
    elif (n-k) > k:
        return fakultet(n, (n-k)) // fakultet(k, 1)
    else:
        return fakultet(n,k)




