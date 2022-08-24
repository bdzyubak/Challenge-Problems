
def tower_breakers(n, m):
    # if n % 2 == 0: 
    #     towers_odd = 1
    # else: 
    #     towers_odd = 0
    # moves = list()
    # moves_tower(m,moves)
    # if len(moves) % 2 == 0: 
    #     moves_odd = 0 
    # else: 
    #     moves_odd = 1
    # overall_odd = towers_odd + moves_odd
    # if overall_odd % 2 == 0: 
    #     return 2
    # else: 
    #     return 1
    
    move_sets = list()
    for i in range(m // 2, 0, -1): 
        
        moves = list()
    moves_tower(m,moves)
    # Add number of towers to variants of moves in one tower 
    # If odd permutation exists - player 1 wins, else player 2

def moves_tower(m,moves): 
    # pattern = list()
    for i in range(m // 2, 0, -1): 
        new_m = m-i
        if m % new_m == 0: 
            moves.append(i)
            moves_tower(new_m,moves)

if __name__ == "__main__": 
    n = 2
    m = 2
    assert tower_breakers(n,m) == 2

    n = 1
    m = 4
    assert tower_breakers(n,m) == 1