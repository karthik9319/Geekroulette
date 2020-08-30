from random import SystemRandom
from variables import dummy_names

cryptogen = SystemRandom()

# class Player():

# def __init__(self,name, guess_number, status, prime):
#     self.name = name
#     self.guess_number = guess_number
#     self.status = status
#     self.prime = prime


# def win(self):
#     if guess_number == win_num:
#         return 1
#     else:
#         return 0

# def odd_even_check(self):
#     if win_num % 2 == 0:
#         return False
#     else:
#         return True

# def prime_no_prime(self):
#     for i in range(2, win_num):
#         if i % 2 == 0:
#             return False
#         else:
# return True


def game_logic():
    big_pot = []
    for i in range(10):
        elem = [cryptogen.randrange(9) for i in range(9)]
        sum_elem = sum(elem)
        big_pot.append(sum_elem)
    win_num = big_pot.index(min(big_pot))
    return win_num


win_num = game_logic()
no_of_players = int(input("No of players (max 5): "))


def odd_check():
    if win_num % 2 == 0:
        return "False"
    else:
        return "True"


def prime_no_prime():
    if win_num > 1:
        if win_num in [2, 3, 5, 7]:
            return "True"
        else:
            return "False"
    else:
        return "False"


def score_check(guess_number, status, prime):
    def test1(guess_number, win_num):
        if guess_number == win_num:
            h = 5
        else:
            h = 0
        return h

    def test2(status):
        status = status.capitalize()
        orig_status = odd_check()
        if status != orig_status:
            return 0
        else:
            return 1

    def test3(prime):
        prime = prime.capitalize()
        orig_prime = prime_no_prime()
        if prime != orig_prime:
            return 0
        else:
            return 1

    x = test1(guess_number, win_num)
    y = test2(status)
    z = test3(prime)
    return x, y, z


# to store player data and input player information
players = []
for i in range(no_of_players):
    print("player {}: ".format(i + 1), dummy_names[i])
    overwrite = input("overwrite (y or n)? : ")
    if overwrite == "y":
        player, guess_number, status, prime = (
            input("Player {}: ".format(i + 1)),
            int(input("Guess number (0-9): ")),
            input("Odd (True or False): "),
            input("Prime (True or False): "),
        )
        # player = Player( input("Player {}: ".format(i+1)), input("Guess number (0-9): "), input("Odd (True or False): "), input("Prime (True or False): "))
        win_status, status, prime = score_check(guess_number, status, prime)
        players.append([player, win_status, status, prime])

    else:
        player, guess_number, status, prime = (
            dummy_names[i],
            int(input("Guess number (0-9): ")),
            input("Odd (True or False): "),
            input("Prime (True or False): "),
        )
        # player = Player( dummy_names[i], input("Guess number (0-9): "), input("Odd (True or False): "), input("Prime (True or False): "))
        win_status, status, prime = score_check(guess_number, status, prime)
        players.append([player, win_status, status, prime])


print(players)
print(win_num)
