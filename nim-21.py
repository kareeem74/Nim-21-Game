# My name is Kareem Hasseeb, Iam student at FCAI_CU <3
# main menu
print("\x1b[1;32;41m" + "           N I M - 2 1          " + "\x1b[0m")
print("Created by Kareem Hasseeb\n")
restart = 1


def turnChecker(n):
    if n % 2 == 0:
        turn = player1
    else:
        turn = player2
    return turn


while restart != "x":
    player1 = input("Enter Player1 Name: ")
    if player1 == "":
        player1 = "Player1"
    player2 = input("Enter Player2 Name: ")
    if player2 == "":
        player2 = "Player2"
    nim = 21
    counter = 0
    print("\n\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n\n")
    print("Enter a number in range [1,3]")
    while nim > 1:
        print("\n", nim, "\n")
        while True:
            try:
                l = int(input("{} turn: ".format(turnChecker(counter))))
            except ValueError:
                print("You must enter a number in range [1,3]")
                continue
            if 0 < l < 4:
                break
            print("The number must be in range [1,3]")

        if nim > l:
            nim -= l
            counter += 1
    print("\n", nim, "\n")
    print("\x1b[6;30;42m" + turnChecker(counter-1), "WINS !" + "\x1b[0m")
    restart = input("press any key to start again, or x to exit. ")
