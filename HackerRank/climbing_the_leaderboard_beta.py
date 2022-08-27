def climbingLeaderboard(ranked,player): 
    print('')
    print('New example (ranked, player): ')
    print(ranked)
    print(player)
    player_ranks = []
    for game in player: 
        print('New score: ' + str(game))
        # idx = binary_search(ranked,game,min_ind=0,max_ind=len(ranked)-1)
        idx = binary_search_resursive(ranked,game,min_ind=0,max_ind=len(ranked)-1)
        score = index_to_rank(ranked,idx)
        print('Score is: ' + str(score))
        player_ranks.append(score)
        ranked.insert(idx,game)
        print('New rank is: ')
        print(ranked)
    print('Player ranks are:')
    print(player_ranks)
    return player_ranks

# def binary_search(ranked,game,min_ind,max_ind): 
#     idx = (max_ind + min_ind) // 2
#     if idx<0: 
#         return 0
#     elif idx>len(ranked)-1: 
#         return len(ranked)
    
#     if game == ranked[idx]: 
#         return idx
#     elif game > ranked[idx]: 
#         idx = binary_search(ranked,game,min_ind=0,max_ind=idx-1) 
#     else: 
#         idx = binary_search(ranked,game,min_ind=idx+1,max_ind=len(ranked)-1) 
#     print('Index is: ' + str(idx))
#     return idx

def binary_search_resursive(arr, x, min_ind, max_ind):
    if max_ind <= 0: 
        return 0
    elif min_ind >= len(arr)-1: 
        return len(arr)
    
    mid = (max_ind + min_ind) // 2
    if max_ind>=min_ind: 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] < x:
            return binary_search_resursive(arr, x, min_ind, mid - 1)

        # Else the element can only be present in right subarray
        else:
            return binary_search_resursive(arr, x, mid + 1, max_ind) 
    else: return mid

def index_to_rank(ranked,idx): 
    return len(set(ranked[:idx])) + 1
          

# def climbingLeaderboard(ranked, player):
#     print('New test case: ')
#     print(ranked)
#     print(player)
#     player_ranks = []
#     for score in player: 
#         mid = len(ranked)//2 - 1
#         i = mid
#         print('Score: ' + str(score))
#         if score == ranked[mid]: 
#             calculate_ran_and_update(ranked,player_ranks,mid,score)
#             continue
#         elif score < ranked[mid]: 
#             while i < len(ranked) and score<=ranked[i]: 
#                 i+= 1
#         elif score > ranked[mid]: 
#             while i > 0 and score>=ranked[i]: 
#                 i-= 1
        
#         print('Location: ' + str(i))
#         calculate_ran_and_update(ranked,player_ranks,i,score)
        
#     return player_ranks

# def calculate_ran_and_update(ranked,player_ranks,i,score): 
#     game_rank = len(set(ranked[:i])) + 1
#     print('Game Rank: ' + str(game_rank))
#     player_ranks.append(game_rank)
#     ranked.insert(i,score)
#     print(ranked)
#     return game_rank

if __name__ == '__main__': 
    ranked = [100,90,90,80]
    player = [70,80,105]
    result = climbingLeaderboard(ranked,player)
    assert result == [4,3,1]
    
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    result = climbingLeaderboard(ranked,player)
    assert result == [6,5,4,2,1]
    print('Done.')