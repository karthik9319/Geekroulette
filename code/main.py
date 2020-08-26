from random import SystemRandom

cryptogen = SystemRandom()
def game_logic():
    big_pot = []
    for i in range(10):
        elem = [cryptogen.randrange(9) for i in range(9)]
        sum_elem = sum(elem)
        big_pot.append(sum_elem)
    win_num = big_pot.index(min(big_pot))
    return win_num


print("place your bets gentlemen")
win_num = game_logic()
player_1 = int(input("player 1: "))
player_2 = int(input("player 2: "))
player_3 = int(input("player 3: "))
bets = [player_1, player_2, player_3]

if win_num in bets:
    print(f" Winner is {bets.index(win_num)}")
else:
    print(f" Sorry people you didn't guess right!!! Lucky number is  {win_num} ")