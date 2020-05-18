class State:
    def __init__(self):
        self.data = []
        self.winner = None
        self.end = False

    def addMove(self,move):
        self.data.append(move)    

    def isEnd(self):
        if self.end is not None:
            return self.end       
        for i in range(0, len(self.data), 2):
            x,y = self.data[i]
            for j in range(i+2, len(self.data), 2):
                x2,y2 = self.data[j]
                if (x == x2 + 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 - 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 and (y == y2-1 or y == y2+1)):
                    xdiff = x-x2
                    ydiff = y-y2
                    for k in range(j+2, len(self.data), 2):
                        x3,y3 = self.data[k]
                        if np.abs(xdiff) == 1 and ydiff == 0:
                            if y == y3 and (x == x3 - xdiff or x2 == x3 + xdiff):
                                self.winner = 1
                                self.end = True
                                return self.end
                        elif xdiff == 0 and np.abs(ydiff) == 1:
                            if x == x3 and (y == y3 - ydiff or y2 == y3 + ydiff):
                                self.winner = 1
                                self.end = True
                                return self.end
                        else:
                            if (x == x3 - xdiff and y == y3 - ydiff) or (x2 == x3 + xdiff and y2 == y3 + ydiff):
                                self.winner = 1
                                self.end = True
                                return self.end
        for i in range(1, len(self.data), 2):
            x,y = self.data[i]
            for j in range(i+2, len(self.data), 2):
                x2,y2 = self.data[j]
                if (x == x2 + 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 - 1 and (y == y2 or y == y2+1 or y == y2-1)) or (x == x2 and (y == y2-1 or y == y2+1)):
                    xdiff = x-x2
                    ydiff = y-y2
                    for k in range(j+2, len(self.data), 2):
                        x3,y3 = self.data[k]
                        if np.abs(xdiff) == 1 and ydiff == 0:
                            if y == y3 and (x == x3 - xdiff or x2 == x3 + xdiff):
                                self.winner = 2
                                self.end = True
                                return self.end
                        elif xdiff == 0 and np.abs(ydiff) == 1:
                            if x == x3 and (y == y3 - ydiff or y2 == y3 + ydiff):
                                self.winner = 2
                                self.end = True
                                return self.end
                        else:
                            if (x == x3 - xdiff and y == y3 - ydiff) or (x2 == x3 + xdiff and y2 == y3 + ydiff):
                                self.winner = 2
                                self.end = True
                                return self.end
        self.end = False
        return self.end
