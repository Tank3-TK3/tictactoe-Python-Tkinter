################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk
from tictactoe_interface import TicTacToeInterface as ti
from tictactoe_class import TicTacToeClass as tc

################################################################################
#                                 MAIN

if __name__ == '__main__':
    root = tk.Tk()
    app = ti( root )
    logi = tc( app )
    logi.events()
    root.mainloop()