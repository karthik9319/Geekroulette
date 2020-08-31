from random import SystemRandom
from tabulate import tabulate
from prettytable import PrettyTable
from variables import dummy_names

cryptogen = SystemRandom()


print(
    "======================================  Game Rules  ========================================="
)
print("1. Select number of players")
print("2. Machine asks you overwrite or use existing name ")
print("3. You have to choose at least one of the four bets available")
print(
    "4. First asks for which category to choose next it will ask for how much amount you wanna bet"
)
print(
    "5. If you're not choosing that particular bet enter 0 in category as well as bet amount"
)
print("6. Choose the number you want to bet in range from 1-36")
print("7. Choose the color either red or black")
print(
    "8. Choose which range the number belongs to Dozen(1-12) Second(13-24) Third(25-36)"
)
print("9. Choose whether is number is odd or not")
print("10. Choose whether the number is prime or not")
print(
    "============================================================================================="
)
print("\n")
print(
    "======================================  Betting Rules  ======================================"
)
print("1: Each player starts with 100$")
print("2: Choosing number will return 5 times the amount")
print("3: Choosing color will return 2 times the amount")
print("4: Choosing range will return 2 times the amount")
print("5: Choosing odd or not will return 2 times the amount")
print("6: Choosing prime or not will return 2 times the amount")
print("\n")
print(
    "=============================================================================================="
)


def game_logic():
    big_pot = []
    for i in range(36):
        elem = [cryptogen.randrange(9) for i in range(9)]
        # print(elem)
        sum_elem = sum(elem)
        big_pot.append(sum_elem)
    win_num = big_pot.index(min(big_pot))
    return win_num + 1


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
    if win_num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        h = "red"
    else:
        h = "black"
    return h


def num_stat():
    if win_num in range(1, 19):
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


def score_check(
    guess_number,
    bet_number,
    choice,
    bet_choice,
    mode,
    bet_mode,
    status,
    bet_status,
    prime,
    bet_prime,
):
    def test1(guess_number, bet_number):
        if guess_number == win_num:
            h = 5
        else:
            h = 0
        return h * bet_number

    def test2(choice, bet_choice):
        orig_choice = red_black()
        if choice != orig_choice:
            h = 0
        else:
            h = 2
        return h * bet_choice

    def test3(option, bet_mode):
        orig_option = num_range()
        if option != orig_option:
            h = 0
        else:
            h = 2
        return h * bet_mode

    def test4(status, bet_status):
        status = status.capitalize()
        orig_status = odd_check()
        if status != orig_status:
            h = 0
        else:
            h = 2
        return h * bet_status

    def test5(prime, bet_prime):
        prime = prime.capitalize()
        orig_prime = prime_no_prime()
        if prime != orig_prime:
            h = 0
        else:
            h = 2
        return h * bet_prime

    win_status = test1(guess_number, bet_number)
    choice = test2(choice, bet_choice)
    mode = test3(mode, bet_mode)
    status = test4(status, bet_status)
    prime = test5(prime, bet_prime)

    return win_status, choice, mode, status, prime


def score_print(players):
    t = PrettyTable([
                    "Players",
                    "Guess number",
                    "red/black",
                    "range",
                    "odd",
                    "prime",
                ])
    t.add_row([
        "Original values",
        win_num,
        red_black(),
        num_range(),
        odd_check(),
        prime_no_prime(),
    ])
    for i in range(len(players)):
        t.add_row([
                        players[i][0],
                        str(players[i][1]) + "$",
                        str(players[i][2]) + "$",
                        str(players[i][3]) + "$",
                        str(players[i][4]) + "$",
                        str(players[i][5]) + "$",
                    ])
    print(t)








# to store player data and input player information
players = []
for i in range(no_of_players):
    print("player {}: ".format(i + 1), dummy_names[i])
    overwrite = input("overwrite Player name(y or n)? : ")
    if overwrite == "y":
        (
            player,
            guess_number,
            bet_number,
            choice,
            bet_choice,
            mode,
            bet_mode,
            status,
            bet_status,
            prime,
            bet_prime,
        ) = (
            input("Player {}: ".format(i + 1)),
            int(input("choose number (1-36): ")),
            int(input("Bet amount: ")),
            input("Red or Black: "),
            int(input("Bet amount: ")),
            input("Dozen(1-12) \nSecond(13-24) \nThird(25-36): "),
            int(input("Bet amount: ")),
            input("Odd (True or False): "),
            int(input("Bet amount: ")),
            input("Prime (True or False): "),
            int(input("Bet amount: ")),
        )
        win_status, choice, mode, status, prime = score_check(
            guess_number,
            bet_number,
            choice,
            bet_choice,
            mode,
            bet_mode,
            status,
            bet_status,
            prime,
            bet_prime,
        )
        players.append([player, win_status, choice, mode, status, prime])

    else:
        (
            player,
            guess_number,
            bet_number,
            choice,
            bet_choice,
            mode,
            bet_mode,
            status,
            bet_status,
            prime,
            bet_prime,
        ) = (
            dummy_names[i],
            int(input("choose number (1-36): ")),
            int(input("Bet amount: ")),
            input("Red or Black: "),
            int(input("Bet amount: ")),
            input("Dozen(1-12) \nSecond(13-24) \nThird(25-36): "),
            int(input("Bet amount: ")),
            input("Odd (True or False): "),
            int(input("Bet amount: ")),
            input("Prime (True or False): "),
            int(input("Bet amount: ")),
        )

        win_status, choice, mode, status, prime = score_check(
            guess_number,
            bet_number,
            choice,
            bet_choice,
            mode,
            bet_mode,
            status,
            bet_status,
            prime,
            bet_prime,
        )
        players.append([player, win_status, choice, mode, status, prime])



score_print(players)
# winner(players)

#todo prettytable
#todo https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data