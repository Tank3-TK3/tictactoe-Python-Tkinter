################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk
from tkinter import font
import random

################################################################################
#                                CLASS

class TicTacToeInterface( tk.Frame ):
    root = None
    fontTitles = None
    fontText = None
    frameOne = None
    frameBoard = None
    canvasBoard = None
    frameTwo = None
    txtTitle = None
    frameButtons = None
    buttons = None

    def __init__( self , root=None ):
        tk.Frame.__init__( self , root )
        self.root = self.drawRoot( root )
        self.fontTitles = tk.font.Font( family="Arial" , size=25)
        self.fontText = tk.font.Font( family="Arial" , size=15)
        self.frameOne = self.drawFrameOne()
        self.frameBoard = self.drawFrameBoard()
        self.canvasBoard = self.drawCanvasBoard()
        #self.frameTwo = self.drawFrameTwo()
        #self.txtTitle = self.drawTextTitle()
        #self.frameButtons = self.drawFrameButtons()
        #self.buttons = self.drawButtons()

    
    def drawRoot( self , root ):
        root.title( "Tic-Tac-Toe (v1.0)" )
        root.geometry( "1280x720+50+50" )
        root.iconbitmap( "./img/tictactoe.ico" )
        root.config( background="#FFFFFF" )
        root.resizable( width=False , height=False )
        return root

    def drawFrameOne( self ):
        frameOne = tk.Frame( self.root , background="#000000" )
        frameOne.pack_propagate( 0 )
        frameOne.pack( fill='both' , side='left' , expand='True' )
        return frameOne

    def drawFrameBoard( self ):
        frameBoard = tk.Frame( self.frameOne , background="#FFFFFF" )
        frameBoard.config( width="600" , height="600" )
        frameBoard.pack_propagate( 0 )
        frameBoard.pack( padx=20 , pady=60 )
        return frameBoard

    def drawCanvasBoard( self ):
        canvasBoard = tk.Canvas( self.frameBoard , background="#444444" )
        canvasBoard.config( bd=0 , highlightthickness=0 , relief='ridge' )
        canvasBoard.pack_propagate( 0 )
        canvasBoard.pack( fill='both' , side='left' , expand='True' )
        for i in range( 200 , 600 , 200 ):
            canvasBoard.create_line( i , 0 , i , 600 , fill="#FFFFFF" )
            canvasBoard.create_line( 0 , i , 600 , i , fill="#FFFFFF" )
        return canvasBoard

    def drawFrameTwo( self ):
        frameTwo = tk.Frame( self.root , background="#222222" )
        frameTwo.pack_propagate( 0 )
        frameTwo.pack( fill='both' , side='left' , expand='True' )
        return frameTwo

    def drawTextTitle( self ):
        txtTitle = tk.Label( self.frameTwo , foreground="#FFFFFF" , background="#222222" )
        txtTitle.config( text="Tic-Tac-Toe" , font=self.fontTitles )
        txtTitle.pack_propagate( 0 )
        txtTitle.pack( fill='x' , side='top' )
        return txtTitle

    def drawFrameButtons( self ):
        frameButtons = tk.Frame( self.frameTwo ,  background="#222222")
        frameButtons.config( height="100" )
        frameButtons.pack_propagate( 0 )
        frameButtons.pack( fill='x' , side='bottom' )
        return frameButtons

    def drawButtons( self ):
        buttons = [ ["1 vs 1"] , ["1 vs AI"] , ["Start"] , ["Exit"] ]
        for i in buttons:
            i.append( tk.Button( self.frameButtons , text=i[0] , font=self.fontText ) )
            i[1].config( background="#666666" , foreground="#FFFFFF" )
            i[1].pack_propagate( 0 )
            i[1].pack( fill='both' , side='left' , expand='True' , padx=20 , pady=20 )
        return buttons

    def drawX( self , j ):
        if j[6][0] == None or j[6][1] == None or j[6][2] == None or j[6][3] == None:
            j[6][0] = self.canvasBoard.create_line( j[1]+50 , j[2]+50 , j[3]-50 , j[4]-50 )
            j[6][1] = self.canvasBoard.create_line( j[3]-50 , j[2]+50 , j[1]+50 , j[4]-50 )
            self.canvasBoard.itemconfig( j[6][0] , fill="#FFFFFF" , width="10" )
            self.canvasBoard.itemconfig( j[6][1] , fill="#FFFFFF" , width="10" )
            j[6][2] = self.canvasBoard.create_line( j[1]+55 , j[2]+55 , j[3]-55 , j[4]-55 )
            j[6][3] = self.canvasBoard.create_line( j[3]-55 , j[2]+55 , j[1]+55 , j[4]-55 )
            self.canvasBoard.itemconfig( j[6][2] , fill="#000000" , width="2" )
            self.canvasBoard.itemconfig( j[6][3] , fill="#000000" , width="2" )
        else:
            self.canvasBoard.itemconfig( j[6][0] , fill="#FFFFFF" , width="10" )
            self.canvasBoard.itemconfig( j[6][1] , fill="#FFFFFF" , width="10" )
            self.canvasBoard.itemconfig( j[6][2] , fill="#000000" , width="2" )
            self.canvasBoard.itemconfig( j[6][3] , fill="#000000" , width="2" )
        j[5] = 1
    
    def drawO( self , j ):
        if j[7][0] == None or j[7][1] == None:
            j[7][0] = self.canvasBoard.create_oval( j[1]+50 , j[2]+50 , j[3]-50 , j[4]-50 )
            j[7][1] = self.canvasBoard.create_oval( j[1]+50 , j[2]+50 , j[3]-50 , j[4]-50 )
            self.canvasBoard.itemconfig( j[7][0] , width=10, outline="#FFFFFF" )
            self.canvasBoard.itemconfig( j[7][1] , width=2, outline="#000000" )
        else:
            self.canvasBoard.itemconfig( j[7][0] , width=10, outline="#FFFFFF" )
            self.canvasBoard.itemconfig( j[7][1] , width=2, outline="#000000" )
        j[5] = -1

    def drawNone( self , j ):
        self.canvasBoard.itemconfig( j[6][0] , fill="#444444" , width="10" )
        self.canvasBoard.itemconfig( j[6][1] , fill="#444444" , width="10" )
        self.canvasBoard.itemconfig( j[6][2] , fill="#444444" , width="2" )
        self.canvasBoard.itemconfig( j[6][3] , fill="#444444" , width="2" )
        self.canvasBoard.itemconfig( j[7][0] , width=10, outline="#444444" )
        self.canvasBoard.itemconfig( j[7][1] , width=2, outline="#444444" )
        j[5] = 0

    def __del__( self ):
        return 0