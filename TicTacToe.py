play = True

# This is the layout of the board
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

print(printBoard(theBoard))

# This is the dictionary with player 1 and player 2. The largest number is the one that its turn is to go.
# Each turn the value of 1 will switch from each player upon picking a x or o.
playerKey = {'Player 1': 1, 'Player 2': 0}
activePlayer = max(playerKey, key=playerKey.get)

# The actual game
def playGame():
    i = 0
    global play
    global playerKey
    global theBoard
    global activePlayer


# This determines if the game is over or not
    def gamePlay():
        global play
        global theBoard
        if theBoard['1'] == ('X') and theBoard['2'] == ('X') and theBoard['3'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['1'] == ('X') and theBoard['5'] == ('X') and theBoard['9'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['1'] == ('X') and theBoard['4'] == ('X') and theBoard['7'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['2'] == ('X') and theBoard['5'] == ('X') and theBoard['8'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['3'] == ('X') and theBoard['6'] == ('X') and theBoard['9'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['4'] == ('X') and theBoard['5'] == ('X') and theBoard['6'] == ('X'):
            print('Player 1 wins')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['7'] == ('X') and theBoard['8'] == ('X') and theBoard['9'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['3'] == ('X') and theBoard['5'] == ('X') and theBoard['7'] == ('X'):
            print('Player 1 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['1'] == ('O') and theBoard['2'] == ('O') and theBoard['3'] == ('O'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['1'] == ('X') and theBoard['5'] == ('X') and theBoard['9'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['1'] == ('X') and theBoard['4'] == ('X') and theBoard['7'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['2'] == ('X') and theBoard['5'] == ('X') and theBoard['8'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['3'] == ('X') and theBoard['6'] == ('X') and theBoard['9'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['4'] == ('X') and theBoard['5'] == ('X') and theBoard['6'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['7'] == ('X') and theBoard['6'] == ('8') and theBoard['9'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()
        elif theBoard['3'] == ('X') and theBoard['5'] == ('X') and theBoard['7'] == ('X'):
            print('Player 2 wins!')
            play = False
            print(printBoard(theBoard))
            restart()


# This is the function that allows the game to restart
    def restart():
        global theBoard
        global playerKey
        global play
        global activePlayer
        global i
        if input('New Game (Yes or No)?') == 'Yes':
            theBoard = {'1': ' ', '2': ' ', '3': ' ',
                        '4': ' ', '5': ' ', '6': ' ',
                        '7': ' ', '8': ' ', '9': ' '}
            playerKey['Player 2'] = 0
            playerKey['Player 1'] = 1
            activePlayer = max(playerKey, key=playerKey.get)
            play = True
            i = 0

# This makes sure if the field is filled the game restarts
    if i == 9:
        restart()

# This is how input is added when the game is playing
    while play == True:
        global activePlayer
        global playerKey
        move = int(input('Which spot would ' + activePlayer + ' like to go?'))

        if playerKey['Player 1'] == 1:
            theBoard[str(move)] = 'X'
            playerKey['Player 1'] = 0
            playerKey['Player 2'] = 1
            activePlayer = max(playerKey, key=playerKey.get)

            gamePlay()
            i += 1
        else:
            theBoard[str(move)] = 'O'
            playerKey['Player 2'] = 0
            playerKey['Player 1'] = 1
            activePlayer = max(playerKey, key=playerKey.get)
            gamePlay()
            i += 1
        print(printBoard(theBoard))

playGame()
