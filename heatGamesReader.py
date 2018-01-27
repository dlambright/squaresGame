

class heatGamesReader:

    def __init__(self):
        self.averageScore = 0
        # probaly need to put something about a huge-ass list of the moves.  tbd.

    def getAverageBoardScores(self):
        total = 0
        for i in range(0, 20001):
            total = total + HGR.getScoreForGame("games/" + str(i) + ".sqgm")

        total = total / 20000.0
        return total

    def getScoreForGame(self, fileToReadIn):
        with open(fileToReadIn, "r+") as openFile:
            fileString = openFile.readlines()
            return int(fileString[len(fileString)-1])


    def getMovesForGame(self, fileToReadIn):
        with open(fileToReadIn, "r+") as openFile:
        fileString = openFile.readlines()
        return int(fileString[len(fileString)-1])



#HGR = heatGamesReader()

