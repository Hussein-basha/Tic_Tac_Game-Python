# create GameBoard class
class GameBoard():
    # inside the GameBoard class we create instance of the game board as follows : 
    def __init__(self):
        self.game_board = {1:' ' , 2:' ' ,3:' ' , 4:' ' , 5:' ' , 6:' ' , 7:' ' , 8:' ' , 9:' '}
    # then we create ites as items setter function :
    def set_items(self , user , position , game_board):
        game_board[position] = user
        return game_board
    # create a decorator (@property) for the gameBoard function to add seperate self instance for game_board: 
    @property
    def gameBoard(self):
        return self.game_board
    # add another function is called ClearBoard:
    def ClearBoard(self):  
        self.game_board = {1:' ' , 2:' ' , 3:' ' , 4:' ' , 5:' ' , 6:' ' , 7:' ' , 8:' ' , 9:' '}
    # add another function is called Is_Take_Place:
    def Is_Place_Taken(self , game_board , index):
        if game_board[index] != ' ':
            return True
    # add another function is called Is_Board_Full:
    def Is_Board_Full(self , game_board):
        for index in range(1 , 10):
            if game_board[index] == ' ':
                return False
        return True
     # add another function is called Is_Game_won:
    def Is_Game_Won(self , game_board):
        win_conds = ((1 , 2 , 3) , (4 , 5 , 6) , (7 , 8 , 9) , (1 , 4 , 7) , (2 , 5 , 8) , (3 , 6 , 9) , (1 , 5 , 9) , (3 , 5 , 7))
        for win_cond in win_conds:
            if game_board[win_cond[0]] == game_board[win_cond[1]] and game_board[win_cond[1]] == game_board[win_cond[2]] and game_board[win_cond[0]] != ' ' :
                return True
    # add another Function to print GameBoard 
    def PrintBoard(self , game_board):
        index = 0
        for row in range(1 , 4):
            for column in range(1 , 4):
                index += 1
                if column != 3:
                    print(game_board[index] , end=' ')
                    print('|' , end=' ')
                else:
                    print(game_board[index])

# create a second class called Game:to control the game start and game end. and ask for players names 
class Game():
    # 1- game start
    def game_start(self):
        self.controlBoard = GameBoard()
        self.game_board = self.controlBoard.gameBoard
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print("Welcom To X-O Game")
        print("Please Enter Player One's name")
        self.player_one = input(' : ')
        print("Please Enter Player Two's name")
        self.player_two = input(' : ')
        print("Here is your game board , each place is represented by 1-9 , staring from left column each time and moving along the row")
        self.controlBoard.PrintBoard(self.game_board)
        self.turn = 1

    # 3- game end and play again
    def game_end(self):
        # check if a player wants to end the game 
        if self.game_running == False:
            replay = input("Press 0 To Quit Or 1 To Play Again : ")
            try:
                if int(replay):
                    self.game_running = True
                    self.game_start()
            except:
                print("A Number Must Be Entered")
                self.game_end()
    # 4- game turn
    def takeTurn(self , user , item):
        print(user + " Choose A Place , 1-9 ")
        try:
            position = int(input(' : '))
            if position > 9 or position < 1 :
                raise Exception
        except:
            print("Pick a number between 1-9")
            return self.takeTurn(user , item)
        if self.controlBoard.Is_Place_Taken(self.game_board , position):
            print("That Place Is Taken")
            self.takeTurn(user , item)
        else:
            self.controlBoard.set_items(item , position , self.game_board)
            self.controlBoard.PrintBoard(self.game_board)
            if self.controlBoard.Is_Game_Won(self.game_board):
                print(user + " Wins. ")
                self.game_running = False
    # 4-game manager
    def main(self): 
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn %2 != 0:
                self.takeTurn(self.player_one , 'O')
            else:
                self.takeTurn(self.player_two , 'X')

            if self.controlBoard.Is_Board_Full(self.game_board):
                print("It's a draw!! You both lose!")
                self.game_running = False
            self.turn += 1

            if not self.game_running:
                self.game_end()


if __name__ == '__main__':
    Game().main()





