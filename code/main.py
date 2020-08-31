from random import SystemRandom

from variables import dummy_names

cryptogen = SystemRandom()




print("======================  Game Rules  ==================================")
print("Step 1: Select number of players")
print("Step 2: Machines asks you overwrite or use existing name ")
print("Step 3: Choose the number you want to bed in range from 1-36")
print("Step 4: Choose the color either red or black")
print("Step 5: Choose which range the number belongs to Dozen(1-12) Second(13-24) Third(25-36)")
print("Step 6: Choose whether the number is prime or not")
print("=======================================================================")


def game_logic():
    big_pot = []
    for i in range(36):
        elem = [cryptogen.randrange(9) for i in range(9)]
        # print(elem)
        sum_elem = sum(elem)
        big_pot.append(sum_elem)
    win_num = big_pot.index(min(big_pot))
    return win_num+1


win_num = game_logic()
no_of_players = int(input("No of players (max 5): "))
print(win_num)

def odd_check():
    if win_num > 0:
        if win_num % 2 == 0:
            return "False"
        else:
            return "True"
    else:
        return "False"


def prime_no_prime():
    if win_num > 1:
        if win_num in [2, 3, 5, 7]:
            return "True"
        else:
            return "False"
    else:
        return "False"


def red_black():
    if win_num in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        h = "red"
    else:
        h = "black"
    return h


def num_stat():
    if win_num in range(1,19):
        h = "low"
    else:
        h = "high"
    return h


def num_range():
    if win_num in range(1, 13):
        h = "dozen"
    elif win_num in range(13, 25):
        h = "second"
    elif win_num in range(25, 37):
        h = "third"
    return h

def score_check(guess_number, choice, mode, status, prime):
    
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

    def test4(choice):
        orig_choice = red_black()
        if choice != orig_choice:
            return 0
        else:
            return 1

    def test5(option):
        orig_option = num_stat()
        if option != orig_option:
            return 0
        else:
            return 1
    
    win_status = test1(guess_number, win_num)
    status = test2(status)
    prime = test3(prime)
    choice = test4(choice)
    mode = test5(mode)
    
    return win_status, status, prime, choice, mode



# def winner(players):
#     for i in range(len(players)):
#         x = players[i]
#         if x[1] == 5:
#             print("Guessed right: ", x[0])
#             print("Roulette Number: ", win_num)
#         if x[2] == 1:
#             print("Lucky you!! ", x[0])
#             print("Roulette Number: ", win_num)
#         if x[3] == 1:
#             print("Awesome Guess: ", x[0])
#             print("Roulette Number: ", win_num)
            


# to store player data and input player information
players = []
for i in range(no_of_players):
    print("player {}: ".format(i + 1), dummy_names[i])
    overwrite = input("overwrite Player name(y or n)? : ")
    if overwrite == "y":
        player, guess_number, choice, mode, status, prime = (
            input("Player {}: ".format(i + 1)),
            int(input("Guess number (1-36): ")),
            input("Red or Black: "),
            input("Dozen(1-12) \n Second(13-24) \n Third(25-36): "),
            input("Odd (True or False): "),
            input("Prime (True or False): "),
        )
        win_status, choice, mode, status, prime = score_check(guess_number, choice, mode, status, prime)
        players.append([player, win_status, choice, mode, status, prime])

    else:
        player, guess_number, choice, mode, status, prime = (
            dummy_names[i],
            int(input("Guess number (1-36): ")),
            input("Red or Black: "),
            input("Dozen(1-12) \nSecond(13-24) \nThird(25-36): "),
            input("Odd (True or False): "),
            input("Prime (True or False): "),
        )
        win_status, choice, mode, status, prime = score_check(guess_number, choice, mode, status, prime)
        players.append([player, win_status, choice, mode, status, prime])


print(players)

# winner(players)

