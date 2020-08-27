from random import SystemRandom

cryptogen = SystemRandom()

class Player():
    def __init__(self):
        num = int(input("No of Players: "))
        return num
        
    def player_name(self):
        for i in range(num):
            self.player_i = input("Player1: ")
            print(player_i)
    
    # def num_players(self):
    #     self.num = num


a = Player()
# b = Player.player_name("karthik")
# c = Player.player_name("kishore")
print(a)     
        
        
        
        
        
        
        
# def game_logic():
#     big_pot = []
#     for i in range(10):
#         elem = [cryptogen.randrange(9) for i in range(9)]
#         sum_elem = sum(elem)
#         big_pot.append(sum_elem)
#     win_num = big_pot.index(min(big_pot))
#     return win_num

# def odd_even_check(win_num): 
#     if win_num % 2 == 0:
#         return True
#     else:
#         return False

# def win_check():
#     if win_num in player_bets:
#         return f" Winner is Player_{player_bets.index(win_num)+1}"
#     else:
#         return f" Sorry people you didn't guess right!!! Lucky number is  {win_num} "
    
# def status_bets_check(status):
#     winners = [i for i in range(len(status_bets)) if status_bets[i] == status ]
#     for i in range(len(winners)):
#         return f" Good thing you guessed this right at least", players[winners[i]]


# win_num = game_logic()

# def get_players(num: int) -> int:
#     for i in range(num):
        


# players = ['player_1', 'player_2', 'player_3']
# print("place your bets gentlemen")
# player_1 = int(input("player 1: "))
# player_2 = int(input("player 2: "))
# player_3 = int(input("player 3: "))
# player_bets = [player_1, player_2, player_3]


# print("place your guess even or odd")
# status_player_1 = (input("player 1: "))
# status_player_2 = (input("player 2: "))
# status_player_3 = (input("player 3: "))
# player_status = [status_player_1, status_player_2, status_player_3]
# status_bets = [True if player_status[i].lower() == 'even' else False for i in range(len(player_status)) ]



# status = odd_even_check(win_num)




# print(win_num)


    
# print(win_check())
# print(status_bets_check(status))