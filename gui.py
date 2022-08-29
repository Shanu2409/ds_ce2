from tkinter import *
from solve import solver

root = Tk()
root.title("Sudoku S0lver")
root.geometry("324x550")

label = Label(root,text="FIll in the numbers.").grid(row=0,column=1,columnspan=10)

erLab = Label(root, text="", fg="red")
erLab.grid(row=15,column=1,columnspan=10, pady=5)

solvLab = Label(root, text="", fg="green")
solvLab.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

def validNum(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out

reg = root.register(validNum)

def draw3(row, col, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width=5, bg=bgcolor, justify=CENTER, validate='key', validatecommand=(reg, "%P"))
            # e.insert(0,)
            e.grid(row=row+i+1, column=col+j+1, sticky="nsew", padx=1,pady=1, ipady=5)
            cells[(row+i+1,col+j+1)] = e

def draw9():
    color = "#D0ffff"
    for rown in range(1,10,3):
        for coln in range(0,9,3):
            draw3(rown,coln,color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

def clearVal():
    erLab.config(text="")
    solvLab.config(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

def getVal():
    board = []
    erLab.configure(text="")
    solvLab.configure(text="")

    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateVal(board)

btn = Button(root, command=getVal, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn2 = Button(root, command=clearVal, text="Clear", width=10)
btn2.grid(row=20, column=5, columnspan=5, pady=20)

def updateVal(s):
    sol = solver(s)
    if sol!= "NO":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        solvLab.configure(text="Sudoku solved!!")
    else:
        erLab.configure(text="No solution..")


draw9()
root.mainloop()