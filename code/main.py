import csv
import datetime
from random import SystemRandom

from prettytable import PrettyTable  # type: ignore
from tqdm import tqdm  # type: ignore

from variables import dummy_names

cryptogen = SystemRandom()
x = datetime.datetime.now()

print("\n")
print("Welcome to GeekRoulette for us coders!!!")
print("\n")

print(
    "======================================  Game Rules  ========================================="
)
print("1. Select number of players")
print("2. Machine asks you overwrite or use existing name ")
print("3. You have to choose at least one of the four bets available")
print(
    "4. First asks for which category to choose next it will ask for how much amount you wanna bet"
)
print("5: If you exceed the amount 100$ you can't bet on that category")
print("6: At each step machine shows how much money you left")
# print(
#     "5. If you're not choosing that particular bet enter 0 in category as well as bet amount"
# )
# print("6. Choose the number you want to bet in range from 1-36")
print("7: Numbers belonging to red are 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 and 36")
print("8: Numbers belonging to black are 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33 and 35")
print("9. Choose the color either red or black")
print(
    "10. Choose which range the number belongs to Dozen(1-12) Second(13-24) Third(25-36)"
)
print("11. Choose whether is number is odd or not")
print("12. Choose whether the number is prime or not")
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
        sum_elem = sum(elem)
        big_pot.append(sum_elem)
    win_num = big_pot.index(min(big_pot))
    return win_num + 1


win_num = game_logic()
print("\n")
no_of_players = int(input("No of players: "))
print("\n")
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
    t = PrettyTable(
        [
            "Players",
            "Guess number",
            "red/black",
            "range",
            "odd",
            "prime",
            "Total winnings",
        ]
    )
    for i in range(len(players)):
        total = (
            players[i][1]
            + players[i][2]
            + players[i][3]
            + players[i][4]
            + players[i][5]
        )
        t.add_row(
            [
                players[i][0],
                str(players[i][1]) + "$",
                str(players[i][2]) + "$",
                str(players[i][3]) + "$",
                str(players[i][4]) + "$",
                str(players[i][5]) + "$",
                str(total) + "$",
            ]
        )
    print(t)


def orig_print():
    print("Original Values")
    t = PrettyTable(["Guess number", "red/black", "range", "odd", "prime"])
    t.add_row(
        [win_num, red_black(), num_range(), odd_check(), prime_no_prime()]
    )

    print(t)


def player_print(players_orig):
    t = PrettyTable(
        [
            "Players",
            "Guess number",
            "Bet amount1",
            "red/black",
            "Bet amount2",
            "range",
            "Bet amount3",
            "odd",
            "Bet amount4",
            "prime",
            "Bet amount5",
        ]
    )
    for i in range(len(players_orig)):
        t.add_row(
            [
                players_orig[i][0],
                players_orig[i][1],
                str(players_orig[i][2]) + "$",
                players_orig[i][3],
                str(players_orig[i][4]) + "$",
                players_orig[i][5],
                str(players_orig[i][6]) + "$",
                players_orig[i][7],
                str(players_orig[i][8]) + "$",
                players_orig[i][9],
                str(players_orig[i][10]) + "$",
            ]
        )
    print(t)


def amount_check(number):
    if number > 100:
        print("Amount exceeded by {}, Max allowed is 100$: ".format(number - 100))
        number = int(input("Bet amount: "))
        amount_check(number)
    else:
        pass
    return number


# to store player data and input player information
players = []
players_orig = []
for i in range(no_of_players):
    print("\n")
    print("default player name {}: ".format(i + 1), dummy_names[i])
    overwrite = input("overwrite Player name(y or n)? : ")
    if overwrite == "y":
        player = input("Player {}: ".format(i + 1))
        print("\n")
        guess_number = int(input("choose number (1-36): "))
        bet_number = amount_check(int(input("Bet amount: ")))
        print("\n")
        choice = input("Red or Black: ")
        if bet_number < 100:
            print("Amount remaining: ", 100 - bet_number)
            bet_choice = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_choice = 0
        print("\n")
        mode = input("Dozen(1-12) \nSecond(13-24) \nThird(25-36): ")
        if bet_number + bet_choice < 100:
            print("Amount remaining: ", 100 - (bet_number + bet_choice))
            bet_mode = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_mode = 0
        print("\n")
        status = input("Odd (True or False): ")
        if bet_number + bet_choice + bet_mode < 100:
            print("Amount remaining: ", 100 - (bet_number + bet_choice + bet_mode))
            bet_status = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_status = 0
        print("\n")
        prime = input("Prime (True or False): ")
        if bet_number + bet_choice + bet_mode + bet_status < 100:
            print(
                "Amount remaining: ",
                100 - (bet_number + bet_choice + bet_mode + bet_status),
            )
            bet_prime = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_prime = 0

        players_orig.append(
            [
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
            ]
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
        player = dummy_names[i]
        print("\n")
        guess_number = int(input("choose number (1-36): "))
        bet_number = amount_check(int(input("Bet amount: ")))
        print("\n")
        choice = input("Red or Black: ")
        if bet_number < 100:
            print("Amount remaining: ", 100 - bet_number)
            bet_choice = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_choice = 0
        print("\n")
        mode = input("Dozen(1-12) \nSecond(13-24) \nThird(25-36): ")
        if bet_number + bet_choice < 100:
            print("Amount remaining: ", 100 - (bet_number + bet_choice))
            bet_mode = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_mode = 0
        print("\n")
        status = input("Odd (True or False): ")
        if bet_number + bet_choice + bet_mode < 100:
            print("Amount remaining: ", 100 - (bet_number + bet_choice + bet_mode))
            bet_status = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_status = 0
        print("\n")
        prime = input("Prime (True or False): ")
        if bet_number + bet_choice + bet_mode + bet_status < 100:
            print(
                "Amount remaining: ",
                100 - (bet_number + bet_choice + bet_mode + bet_status),
            )
            bet_prime = int(input("Bet amount: "))
        else:
            print("sorry you used up all 100$")
            bet_prime = 0

        players_orig.append(
            [
                dummy_names[i],
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
            ]
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


print(
    "============================================================================================================================="
)
print("\n")
player_print(players_orig)
# print(len(players_orig[0]))
print("\n")
for i in tqdm(range(10000000), desc="Spinning the lucky wheel"):
    pass
print("\n")
print(
    "=============================================================================================================================="
)
orig_print()
print("\n")
print(
    "=============================================================================================================================="
)
print("\n")
score_print(players)


fields = [
    "Date",
    "Time",
    "Players",
    "Guess number",
    "Bet amount1",
    "red/black",
    "Bet amount2",
    "range",
    "Bet amount3",
    "odd",
    "Bet amount4",
    "prime",
    "Bet amount5",
    "winnings",
    "original number"
    "Guess number",
    "red/black",
    "range",
    "odd",
    "prime",
    "Total winnings",
]


for i in range(len(players_orig)):
    total = (
        players[i][1] + players[i][2] + players[i][3] + players[i][4] + players[i][5]
    )
    rows = [
        [
            x.strftime("%b %d %Y"),
            x.strftime("%H:%M:%S"),
            players_orig[i][0],
            players_orig[i][1],
            str(players_orig[i][2]) + "$",
            players_orig[i][3],
            str(players_orig[i][4]) + "$",
            players_orig[i][5],
            str(players_orig[i][6]) + "$",
            players_orig[i][7],
            str(players_orig[i][8]) + "$",
            players_orig[i][9],
            str(players_orig[i][10]) + "$",
            "-",
            win_num,
            str(players[i][1]) + "$",
            str(players[i][2]) + "$",
            str(players[i][3]) + "$",
            str(players[i][4]) + "$",
            str(players[i][5]) + "$",
            str(total) + "$",
        ]
    ]

filename = "data_storage_players.csv"

# to write change mode to w or append to a and comment fileds while appending
with open(filename, "a") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    # csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)


# todo resume the game with keeping winnings in track and play
# todo the game until 1 person is left checking anyone going to zero
# todo and eliminating them from the game
