# the board itself
theBoard = {'top-L': ' ', 'top-M' : ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M' : ' ', 'mid-R': ' ','low-L': ' ', 'low-M' : ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-' * 5 )
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-' * 5 )
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

solutions = []

#Choosing player
def choosingPlayer(player):
    while True: 
        player = input("Are you X or O: ").upper()
        if player == 'X':
            return 'x'
        elif player =='O':
            return 'o'
        else:
            print("Thats not X or O. Choose one.")
            continue


