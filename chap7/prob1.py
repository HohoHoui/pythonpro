import random

board = [
        [
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8]
        ]
]

newboard = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

Rnewboard = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

Hanswer = None
Canswer = None

#row, col
d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]

#diagonal
d_d1 = [-1, -1, 1, 1]
d_d2 = [-1, 1, 1, -1]

cnt = 0;

def human():
    while True:
        Hanswer = int(input("Where will you move? <0 - 8>:"))
        if 0 <= Hanswer <= 8:
            for i in range(3):
                for j in range(3):
                    if board[0][i][j] == 'O':
                        print(Hanswer, "is already exist.")
                        break
                   
            else:
                print("Fine..")
                for i in range(3):
                    for j in range(3):
                        if board[0][i][j] == Hanswer:
                            board[0][i][j] = 'O'
                            for i in range(4):
                                next_rows = i + d_x[i]
                                next_cols = i + d_y[i]
                                if (next_rows < 0 or 2 <= next_rows) or (next_cols < 0 or 2 <= next_cols):
                                    continue
                                board[0][next_rows][next_cols] += 1
                                next_drows = i + d_d1[i]
                                next_dcols = i + d_d2[i]
                                if((next_drows < 0 or 2 <= next_drows) or (next_drows < 0 or 2 <= next_dcols)):
                                    continue
                                board[0][next_drows][next_dcols] += 1
                                break
                            break
                    break    
                break
            
        else:
            print("wrong answer. Please enter a number within 0 to 8")

        
    #return board

def computer():
    for i in range(3):
        for j in range(3):
            if 2 <= i or 2 <= j: #maxcol is 2, maxrow is 2
                continue
            if board[0][i][j] < board[0][i+1][j+1]: #descending order
                temp = board[0][i][j]
                temp2 = board[0][i+1][j+1]
                newboard[0][i][j] = temp2
                newboard[0][i+1][j+1] = temp
           #maxnum = newboard[0][i][j] #bigest number
    for i in range(3):
        for j in range(3):
            if newboard[0][0][0] == newboard[0][i][j]:
                if newboard[0][i][j] == ("X" or "O"):
                    continue
                temp = newboard[0][i][j]
                newboard[0][i][j] = newboard[0][i+1][j +1]
                newboard[0][i+1][j+1] = temp

    randnum = random.choice(Rnewboard)
    
    for i in range(3):
        for j in range(3):
            if board[0][i][j] == randnum:
                board[0][i][j] = "X";


    
    
def step():
    for i in range(3):
        for j in range(3):
            if board[0][i][j] == board[0][i][2]:
                print(board[0][i][j])
                continue
            print(board[0][i][j], "|", end = "")

def O_won():
    print('O won!\n')
    print('No, no! It cannot be! Somehow you tricked me, human.')
    print('But never again! I, the computer, so swears it!')
    
    while True:
       aa =  input('\n\nPress the enter key to quit.')
       if aa == '\n':
           break
def X_won():
    print('X won!\n');
    print('As I predicted, human, I am triumphant once more.')
    print('Proof that computer are superior to humans in all regards.')

    while True:
        aa = input('\n\nPress the enter key to quit.')
        if aa == '\n':
            break

print("\tWelcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.")
print("\tThis will be a showdown between your human brain and my silicon processor.")

print("\n\tYou will make your move known by entering a number, 0 - 8. The number")
print("\n\twill correspond to the board position as illustrated:\n")

print("\t\t\t\t0 | 1 | 2")
print("\t\t\t\t----------")
print("\t\t\t\t3 | 4 | 5")
print("\t\t\t\t----------")
print("\t\t\t\t6 | 7 | 8")

print("\n\tPrepare yourself, human. The ultimate battle is about to begin.\n\n")

yourTurn = ""

while True:
    yourTurn =str(input("Do you require the first move? <y/n>:"))
    if yourTurn == 'y':
        break
    elif yourTurn == 'n':
        break

while True:
    if ((board[0][0][0] == board[0][0][1]) and (board[0][0][0]== board[0][0][2])):
        if board[0][0][0] == 'X':
            X_won()
            break
        elif board[0][0][0] == 'O':
            O_won()
            break
    elif((board[0][1][0] == board[0][1][1]) and (board[0][1][0] == board[0][1][2])):
        if board[0][1][0] == 'X':
            X_won()
            break
        elif borad[0][1][0] == 'O':
            O_won()
            break
    elif((board[0][2][0] == board[0][2][1]) and (board[0][2][0] == board[0][2][2])):
        if board[0][2][0] == 'X':
            X_won()
            break
        elif board[0][2][0] == 'O':
            O_won()
            break
    elif((board[0][0][0] == board[0][1][0]) and (board[0][1][0] == board[0][2][0])):
        if board[0][0][0] == 'X':
            X_won()
            break
        elif board[0][0][0] == 'O':
            O_won()
            break
    elif((board[0][0][1] == board[0][1][1]) and (board[0][1][1] == board[0][2][1])):
        if board[0][0][1] == 'X':
            X_won()
            break
        elif board[0][0][1] == 'O':
            O_won()
            break
    elif((board[0][0][2] == board[0][1][2]) and (board[0][1][2] == board[0][2][2])):
        if board[0][0][2] == 'X':
            X_won()
            break
        elif board[0][0][2] == 'O':
            O_won()
            break
    elif((board[0][0][0] == board[0][1][1]) and (board[0][1][1] == board[0][2][2])):
        if board[0][0][0] == 'X':
            X_won()
            break
        elif board[0][0][0] == 'O':
            O_won()
            break
    elif((board[0][2][0] == board[0][1][1]) and (board[0][1][1] == board[0][2][0])):
        if board[0][2][0] == 'X':
            X_won()
            break
        elif board[0][2][0] == 'O':
            O_won()
            break
    elif ('X' or 'O') in board:
        print('draw')
        break;
    if yourTurn == 'y':
        human()
        step()
        computer()
        step()
    elif yourTurn == 'n':
        computer()
        step()
        human()   
        step()
