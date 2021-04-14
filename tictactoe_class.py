################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk

################################################################################
#                                CLASS

class TicTacToeClass():
    app = None
    gameMatrix = None
    neigcount = None
    gameStatus = None

    def __init__( self , app ):
        self.app = app
        self.gameMatrix = self.createDashboardMatrix()
        self.neigcount = 0
        self.gameStatus = False

    def createDashboardMatrix( self ):
        matrix = []
        cont , x , y = 0 , 0 , 0
        for i in range( 0 , 3 ):
            matrix.append( [] )
            for j in range( 0 , 3 ): # ID , X1 , Y1, X2 , Y2 , Status , CanvX , CanvO
                matrix[i].append( [ cont , x , y , x+200 , y+200 , 0 , 
                                    [ None , None , None , None ] , [ None , None ] ] )
                cont += 1
                x += 200
            y += 200
            x = 0
        return matrix

    def clickMouseButtonL( self , event ):
        x, y = event.x, event.y
        for i in self.gameMatrix:
            for j in i:
                if (x > j[1] and x < j[3]) and (y > j[2] and y < j[4]):
                    if j[5] == 0:
                        self.app.drawX(j)
                    else:
                        self.app.drawNone(j)

    def clickMouseButtonR( self , event ):
        x, y = event.x, event.y
        for i in self.gameMatrix:
            for j in i:
                if (x > j[1] and x < j[3]) and (y > j[2] and y < j[4]):
                    if j[5] == 0:
                        self.app.drawO(j)
                    else:
                        self.app.drawNone(j)

    def events( self ):
        self.drawXO()
        self.drawN()
        #self.printGM()
        self.app.canvasBoard.bind( "<Button-1>" , self.clickMouseButtonL )
        self.app.canvasBoard.bind( "<Button-3>" , self.clickMouseButtonR )
        #self.app.buttons[3][1].config( command=self.app.root.destroy )

    def drawXO( self ):
        for i in self.gameMatrix:
            for j in i:
                self.app.drawX(j)
                self.app.drawO(j)
    
    def drawN( self ):
        for i in self.gameMatrix:
            for j in i:
                self.app.drawNone(j)

    def printGM( self ):
        for i in self.gameMatrix:
            for j in i:
                print(j)

    def __del__( self ):
        return 0