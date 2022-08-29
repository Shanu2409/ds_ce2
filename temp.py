from cgitb import reset
from tkinter import *
from tkinter import messagebox
class Sudoku:

    def __init__(self, board):
        flag=True    
        self.duplicate=[] 
        for i in range(9):
            self.duplicate+=[['','','','','','','','','']]
        for i in range(9):
            for j in range(9):
                self.duplicate[i][j]=board[i][j]
        for i in range(9):
            for j in range(9):
                if not (self.isValid(i,j,self.duplicate)): 
                    flag=False
        if flag:
            self.backtrack(board)
        else:
            messagebox.showinfo('Error','The following Grid does not obey the rules')




    def isValid(self,x, y, b):
        if(b[x][y]==''):
            return True
        tmp = b[x][y];
        b[x][y] = 'D'
        for i in range(9):
            if b[i][y] == tmp : return False
        for i in range(9):
            if b[x][i] == tmp : return False
        for i in range(3):
            for j in range(3):
                if b[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp: return False
        b[x][y] = tmp
        return True

    def backtrack(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValid(i, j, board) and self.backtrack(board):
                            return True
                        board[i][j] = ''
                    return False
        return True

class window:
    def __init__(self, toplevel):

        toplevel.resizable(width = False, height = False)
        toplevel.title('Final')

        font = ('Arial', 18)


        self.fr = Frame(toplevel)

        self.fr.pack(ipady = 0, padx = 0)
        self.fr1 = Frame(toplevel)

        self.fr1.pack(ipady = 0, padx = 0)
        self.fr2 = Frame(toplevel)

        self.fr2.pack(ipady = 0, padx = 0)
        self.fr3 = Frame(toplevel)

        self.fr3.pack(ipady = 0, padx = 0)
        self.fr4 = Frame(toplevel)

        self.fr4.pack(ipady = 0, padx = 0)
        self.fr5 = Frame(toplevel)

        self.fr5.pack(ipady = 0, padx = 0)
        self.fr6 = Frame(toplevel)

        self.fr6.pack(ipady = 0, padx = 0)
        self.fr7 = Frame(toplevel)

        self.fr7.pack(ipady = 0, padx = 0)
        self.fr8 = Frame(toplevel)

        self.fr8.pack(ipady = 0, padx = 0)
        self.fr9 = Frame(toplevel)

        self.fr9.pack(ipady = 1, padx = 1)

        self.__board = []
        for i in range(1,10):
            self.__board += [[0,0,0,0,0,0,0,0,0]]

        variable = self.fr
        px = 0
        py = 0
        for i in range(0,9):
            for j in range(0,9):

                if i == 0:
                    variable = self.fr
                if i == 1:
                    variable = self.fr1
                if i == 2:
                    variable = self.fr2
                if i == 3:
                    variable = self.fr3
                if i == 4:
                    variable = self.fr4
                if i == 5:
                    variable = self.fr5
                if i == 6:
                    variable = self.fr6
                if i == 7:
                    variable = self.fr7
                if i == 8:
                    variable = self.fr8

                color = '#ffffd0'
                f_color='black' 

                if j in [3,4,5] and i in [0,1,2,6,7,8]:
                    color = 'black'
                    f_color= '#ffffd0'
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    color = 'black'
                    f_color = '#ffffd0'
                else:
                    color = '#ffffd0'
                    f_color = 'black'
                inp = Entry(variable, width = 2, font = font,fg=f_color, bg = color, cursor = 'arrow',justify=CENTER , borderwidth = 4,
                                          highlightcolor = '#9c2733', highlightthickness = 1, highlightbackground = f_color,
                                          textvar = bd[i][j])
                
                self.__board[i][j] = inp
                self.__board[i][j].pack(side = LEFT, padx = px, pady = py)



        self.btn1 = Button(self.fr9, text = 'Solve', fg = 'blue', font = ('Arial', 13), command = self.solve)
        self.btn1.pack(side = LEFT)

        self.btn2 = Button(self.fr9, text = 'Reset', fg = 'red', font = ('Arial', 13), command = self.reset)
        self.btn2.pack(side = RIGHT)
    
    def solve(self):
        def recolor(self):
            for i in range(9):
                for j in range(9):
                    if bd[i][j].get() != '':
                        self.__board[i][j].configure(bg='#27779c')
        self.correct()
        recolor(self)
        for i in range(9):
            for j in range(9):
                board[i][j]=bd[i][j].get()
        o=Sudoku(board)
        for i in range(9):
            for j in range(9):
                bd[i][j].set(board[i][j])


    def correct(self):
        for i in range(9):
            for j in range(9):
                if bd[i][j].get() == '':
                    continue
                if len(bd[i][j].get()) > 1 or bd[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    bd[i][j].set('')

    def reset(self):
        for i in range(9):
            for j in range(9):
                bd[i][j].set('')
                if j in [3,4,5] and i in [0,1,2,6,7,8]:
                    self.__board[i][j].configure(bg='black')
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    self.__board[i][j].configure(bg='black')
                else:
                    # self.__board[i][j].configure(bg='black')
                    pass


game=Tk()
board=[]
for i in range(1,10):
    board += [[0,0,0,0,0,0,0,0,0]]
bd = []
for i in range(1,10):
    bd += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        bd[i][j] = StringVar(game)
a=window(game)
game.mainloop()