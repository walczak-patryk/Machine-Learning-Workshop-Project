from player import Player, Bot
from state import State
import argparse

# main class of tictactoe game
class Game:
    def __init__(self, p1 = Player(), p2 =Player(), need_for_win = 3, debug = False):
        self.player1 = p1
        self.player2 = p2
        self.state = State( need_for_win)
        self.need_for_win = need_for_win
        self.currentPlayer = None
        self.debug = debug

    # erase all states of game
    def reset(self):
        self.state = State(self.need_for_win)

    # main function of game
    def play(self):
        self.reset()
        self.currentPlayer = self.player1
        while self.state.end != True :
            move = self.currentPlayer.move(self.state)
            if not self.state.addMove((move[0],move[1])):
                continue
            if self.currentPlayer == self.player1 :
                self.currentPlayer = self.player2
            else :
                self.currentPlayer = self.player1  
            self.state.isEnd()
            if(self.debug):
                self.state.printVector()
        if(self.debug):
            print("--- END ---")
            print("Player "+str(self.state.winner)+" wins")

    # traning function
    def train(self, iterations=100000):
        player1Win = 0.0
        player2Win = 0.0
        self.player1.loadPolicy()
        self.player2.loadPolicy()
        for i in range(0, iterations):
            if i%(iterations/100) == 0:
                print("Iteration {:.0%}".format(i/iterations))
            self.play()
            if self.state.winner == 1:
                player1Win += 1
                self.player1.feedReward(1)
                self.player2.feedReward(0)
            if self.state.winner  == 2:
                player2Win += 1
                self.player1.feedReward(0)
                self.player2.feedReward(1)
        print(player1Win / iterations)
        print(player2Win / iterations)
        self.player1.savePolicy()
        self.player2.savePolicy()
        if(player1Win > player2Win):
            return 1
        return 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--iterations", default="100000", help="Iterations for training")
    ap.add_argument("-t", "--train", default="y", help="Choose whether to train or only play")
    ap.add_argument("-s", "--start", default="2", help="Choose whether you want to play first or second (only when not training)")
    ap.add_argument("-n", "--need", default="3", help="Number of symbols in a row to win")
    args = vars(ap.parse_args())
    iter = int(args["iterations"])
    need = int(args["need"])

    if args["train"] == "y":
        # create bots
        b1 = Bot(1)
        b2 = Bot(2)
        game = Game(b1, b2, need_for_win=need)
        game.debug = False
        # training
        better_bot = game.train(iterations=iter)
        # select the better one
        if better_bot == 1 : 
            game.player2 = Player()
        else:
            game.player1 = Player()
        game.debug = True
        # play with our bot
        game.play() 
    else:
        if int(args["start"]) == 1:
            player = Player()
            b2 = Bot(2)
            game = Game(player, b2, need_for_win=need)
        else:
            b1 = Bot(1)
            player = Player()
            game = Game(b1, player, need_for_win=need)
        game.debug = True
        game.play()          
